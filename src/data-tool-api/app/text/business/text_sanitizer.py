import re
import unicodedata
from typing import Optional, Set


class TextSanitizer:
    """
    Static utilities to sanitize text AFTER normalization.

    - sanitize_for_fuzzy: stronger cleaning for token/string-based metrics.
    - sanitize_for_embeddings: light cleaning to preserve signals useful to
      embedding models (punctuation, accents, emojis, digits).
    """

    @staticmethod
    def sanitize_for_fuzzy(
        s: Optional[str],
        *,
        remove_stopwords: Optional[Set[str]] = None,
        min_token_len: int = 1,
        keep_hyphens_apostrophes_inside: bool = True,
    ) -> str:
        """
        Strong cleaning for fuzzy/token-based similarity.

        Steps:
        - Remove HTML tags, URLs, emails, @mentions, #hashtags
        - Remove punctuation (optionally keep inner hyphens/apostrophes within tokens)
        - Optional stopword removal and short-token filtering
        - Collapse whitespace

        Returns:
            A sanitized string suitable for fuzzy matching.
        """
        if s is None:
            return ""

        text = s

        # Remove HTML
        text = re.sub(r"<[^>]+>", " ", text)

        # Remove URLs
        text = re.sub(r"(https?://\S+|www\.\S+)", " ", text)

        # Remove emails
        text = re.sub(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", " ", text)

        # Remove @mentions / #hashtags
        text = re.sub(r"[@#]\w+", " ", text)

        # Remove punctuation (keep inner hyphens/apostrophes if desired)
        if keep_hyphens_apostrophes_inside:
            text = re.sub(r"[^\w\s\-\'’]", " ", text)
            tokens = []
            for tok in text.split():
                # Trim leading/trailing hyphens/apostrophes
                tok = re.sub(r"(^[-'’]+|[-'’]+$)", "", tok)
                if tok:
                    tokens.append(tok)
            text = " ".join(tokens)
        else:
            text = re.sub(r"[^\w\s]", " ", text)

        # Collapse whitespace
        text = re.sub(r"\s+", " ", text).strip()

        # Optional stopword removal / min length filter
        if remove_stopwords or min_token_len > 1:
            sw = remove_stopwords or set()
            text = " ".join(
                t for t in text.split() if (len(t) >= min_token_len and t not in sw)
            )

        return text

    @staticmethod
    def sanitize_for_embeddings(
        s: Optional[str],
        *,
        remove_handles: bool = False,
        remove_html: bool = True,
        remove_urls: bool = True,
        remove_emails: bool = True,
        collapse_whitespace: bool = True,
    ) -> str:
        """
        Light cleaning for embedding models.

        Goal:
        - Remove only noisy artifacts (HTML, URLs, emails, optionally @/# handles)
        - Keep punctuation, accents, emojis, and digits because they carry signal
          for pretrained encoders.

        Returns:
            A lightly sanitized string ready for embedding.
        """
        if s is None:
            return ""

        text = s

        if remove_html:
            text = re.sub(r"<[^>]+>", " ", text)

        if remove_urls:
            text = re.sub(r"(https?://\S+|www\.\S+)", " ", text)

        if remove_emails:
            text = re.sub(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", " ", text)

        if remove_handles:
            text = re.sub(r"[@#]\w+", " ", text)

        if collapse_whitespace:
            text = re.sub(r"\s+", " ", text).strip()

        return text
