from typing import List
import torch
from sentence_transformers import SentenceTransformer


class Vectorizer:
    """
    Vectorizes long texts by:
      1) splitting them into chunks (via an external Chunker),
      2) encoding each chunk with a SentenceTransformer,
      3) pooling chunk embeddings into a single vector.

    This class does NOT cache embeddings.
    """

    def __init__(
        self,
        model: SentenceTransformer,
        chunker,
        pooling: str = "mean",
        normalize_embeddings: bool = True,
        show_progress_bar: bool = False,
    ) -> None:
        """
        Args:
            model: A SentenceTransformer model instance.
            chunker: An object exposing `chunk(text: str) -> List[str]`.
            pooling: Pooling strategy for chunk embeddings: "mean" | "max".
            normalize_embeddings: Whether to L2-normalize embeddings in model.encode.
            show_progress_bar: Whether to show progress bar during encoding.
        """
        self.model = model
        self.chunker = chunker
        self.pooling = pooling
        self.normalize_embeddings = normalize_embeddings
        self.show_progress_bar = show_progress_bar

    def encode(self, text: str) -> torch.Tensor:
        """
        Encode a (normalized) text with long-text handling (no caching).

        Steps:
            - Split into chunks with the provided Chunker.
            - Encode chunks with SentenceTransformer (convert_to_tensor=True).
            - If multiple chunks, pool them into a single vector.
            - If a single chunk, return that embedding directly.

        Returns:
            A 1D torch.Tensor representing the pooled embedding of the text.
        """
        chunks: List[str] = self.chunker.chunk(text)
        embs = self.model.encode(
            chunks,
            convert_to_tensor=True,
            normalize_embeddings=self.normalize_embeddings,
            show_progress_bar=self.show_progress_bar,
        )
        if embs.ndim == 1:
            # Single chunk → already a 1D vector
            return embs
        return self._pool_embeddings(embs)

    def encode_many(self, texts: List[str]) -> torch.Tensor:
        """
        Encode many texts (each may be long) by calling `encode` per text.

        Note:
            This is a simple loop over texts. It keeps memory usage predictable
            when each text expands into many chunks. If you need higher throughput,
            consider micro-batching at the chunk level.

        Returns:
            A 2D torch.Tensor of shape (N, D) where N = len(texts).
        """
        vectors = [self.encode(t) for t in texts]
        return torch.stack(vectors, dim=0)

    def _pool_embeddings(self, embs: torch.Tensor) -> torch.Tensor:
        """
        Pool chunk embeddings into a single vector using the configured strategy.

        Args:
            embs: Tensor of shape (num_chunks, dim)

        Returns:
            A 1D torch.Tensor of shape (dim,)
        """
        if self.pooling == "max":
            return embs.max(dim=0).values
        # default: mean pooling
        return embs.mean(dim=0)
