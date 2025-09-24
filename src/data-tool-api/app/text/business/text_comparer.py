from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Optional

from app.text.business.text_chunker import TextChunker
from app.text.business.text_normalizer import TextNormalizer
from app.text.business.text_vectorizer import Vectorizer
from app.text.business.text_sanitizer import TextSanitizer  # ← added

import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, CrossEncoder
from rapidfuzz import fuzz


@dataclass(frozen=True)
class CompareConfig:
    """
    Configuration parameters for TextComparer behavior.
    """
    embedding_model_name: str = "all-MiniLM-L6-v2"
    crossencoder_model_name: str = "cross-encoder/stsb-TinyBERT-L-4"
    device: Optional[str] = None          # "cuda", "cpu", "mps"… (auto-detect if None)
    use_half: bool = True                 # use float16 on GPU when possible
    chunk_size: int = 256                 # approx words per chunk for long texts
    pooling: str = "mean"                 # "mean" | "max"
    round_ndigits: int = 4                # rounding digits for returned scores


class TextComparer:
    def __init__(
        self,
        embedding_model_name: str = "all-MiniLM-L6-v2",
        crossencoder_model_name: str = "cross-encoder/stsb-TinyBERT-L-4",
        cfg: Optional[CompareConfig] = None,
    ) -> None:
        """
        Initialize embedding and cross-encoder models.

        - Embedding model: fast semantic similarity via vector distance.
        - Cross-Encoder: slower but often more precise; jointly compares sentence pairs.

        Args:
            embedding_model_name: SentenceTransformer checkpoint for embeddings.
            crossencoder_model_name: CrossEncoder checkpoint for pairwise scoring.
            cfg: Optional advanced configuration; if provided, overrides names above.
        """
        # Build configuration (names from args unless cfg is provided)
        if cfg is None:
            cfg = CompareConfig(
                embedding_model_name=embedding_model_name,
                crossencoder_model_name=crossencoder_model_name,
            )
        object.__setattr__(self, "cfg", cfg)

        # Select device
        self.device = cfg.device or ("cuda" if torch.cuda.is_available() else "cpu")

        # Load models
        self.embedding_model = SentenceTransformer(cfg.embedding_model_name, device=self.device)
        if self.device == "cuda" and cfg.use_half:
            # Some models may not support half precision; ignore errors gracefully
            try:
                self.embedding_model = self.embedding_model.half()
            except Exception:
                pass

        self.crossencoder_model = CrossEncoder(cfg.crossencoder_model_name, device=self.device)

        # Initialize utilities from your project
        self.chunker = TextChunker(chunk_size=cfg.chunk_size)
        self.vectorizer = Vectorizer(
            model=self.embedding_model,
            chunker=self.chunker,
            pooling=cfg.pooling,
            normalize_embeddings=True,
            show_progress_bar=False,
        )

    # --------------------- PUBLIC API ---------------------

    def compare_all_methods(self, text1: str, text2: str) -> Dict[str, float]:
        """
        Compare two texts using three strategies at once:
        - Fuzzy (string-level token set ratio)
        - Embedding cosine similarity (vector-based)
        - Cross-Encoder (context-aware pair scoring)

        Returns:
            A dictionary with normalized scores in [0, 1].
        """
        return {
            "fuzzy_score": self.compare_fuzzy(text1, text2),
            "embedding_cosine_score": self.compare_embeddings_cosine(text1, text2),
            "crossencoder_score": self.compare_crossencoder(text1, text2),
        }

    def compare_fuzzy(self, text1: str, text2: str) -> float:
        """
        Compare texts with token-based fuzzy matching (token_set_ratio).

        This metric is more robust than simple character Levenshtein ratio
        to changes in word order and duplicate tokens.

        Returns:
            Score in [0, 1].
        """
        a = TextNormalizer.normalize(text1)
        b = TextNormalizer.normalize(text2)

        # Strong sanitization for fuzzy matching (remove URLs/emails/HTML/punct noise)
        a = TextSanitizer.sanitize_for_fuzzy(a, remove_stopwords=None, min_token_len=1)
        b = TextSanitizer.sanitize_for_fuzzy(b, remove_stopwords=None, min_token_len=1)

        return float(fuzz.token_set_ratio(a, b) / 100.0)

    def compare_embeddings_cosine(self, text1: str, text2: str) -> float:
        """
        Compare texts using cosine similarity of sentence embeddings and rescale to [0, 1].

        Implementation details:
        - Texts are normalized.
        - Long texts are chunked, each chunk encoded, then pooled back to a single vector (Vectorizer).
        - Cosine similarity in [-1, 1] is linearly rescaled to [0, 1] via (cos + 1) / 2.
        - The result is clamped to [0, 1] for numerical stability.

        Returns:
            Score in [0, 1].
        """
        a = TextNormalizer.normalize(text1)
        b = TextNormalizer.normalize(text2)

        # Light sanitization for embeddings (remove only HTML/URLs/emails; keep punctuation/accents)
        a = TextSanitizer.sanitize_for_embeddings(a, remove_handles=False)
        b = TextSanitizer.sanitize_for_embeddings(b, remove_handles=False)

        va = self._embed(a)
        vb = self._embed(b)

        # Raw cosine in [-1, 1]
        cos = F.cosine_similarity(va.unsqueeze(0), vb.unsqueeze(0)).item()

        # Rescale to [0, 1]
        score_01 = (cos + 1.0) / 2.0

        # Clamp and round for stability / consistency
        score_01 = float(max(0.0, min(1.0, score_01)))
        return round(score_01, self.cfg.round_ndigits)

    def compare_crossencoder(self, text1: str, text2: str) -> float:
        """
        Compare texts with a Cross-Encoder that jointly evaluates both inputs.

        Notes:
        - Different checkpoints may output logits, probabilities, or STS-style scores.
        - We post-process outputs to map to [0, 1]:
            * If values fall outside [0, 1], we apply a sigmoid to interpret them as logits.
            * We then clamp to [0, 1] for safety.

        Returns:
            Score in [0, 1].
        """
        a = TextNormalizer.normalize(text1)
        b = TextNormalizer.normalize(text2)

        # Light sanitization also makes sense here (remove HTML/URLs/emails; keep punctuation/accents)
        a = TextSanitizer.sanitize_for_embeddings(a, remove_handles=False)
        b = TextSanitizer.sanitize_for_embeddings(b, remove_handles=False)

        raw = self.crossencoder_model.predict([(a, b)], show_progress_bar=False)[0]
        t = torch.as_tensor(raw, dtype=torch.float32)
        if (t < 0.0) or (t > 1.0):
            t = torch.sigmoid(t)
        score = float(torch.clamp(t, 0.0, 1.0).item())
        return round(score, self.cfg.round_ndigits)

    # --------------------- INTERNAL HELPERS ---------------------

    def _embed(self, text: str) -> torch.Tensor:
        """
        Encode a (normalized) text via the project's Vectorizer (no caching).
        The Vectorizer handles chunking and pooling internally.
        """
        return self.vectorizer.encode(text)
