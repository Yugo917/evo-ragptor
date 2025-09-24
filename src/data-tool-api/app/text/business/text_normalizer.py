import re
import unicodedata
from typing import Optional


class TextNormalizer:
    """
    Static utility class to normalize text for robust comparisons.

    Operations applied (optional, controlled via parameters):
    - Unicode NFKC normalization
    - Case folding
    - Collapse multiple whitespaces
    - Trim leading/trailing spaces
    """

    @staticmethod
    def normalize(
        s: Optional[str],
        apply_casefold: bool = True,
        collapse_spaces: bool = True,
        strip: bool = True,
        unicode_form: str = "NFKC",
    ) -> str:
        """
        Normalize the input string.

        Args:
            s: Input string (can be None).
            apply_casefold: Whether to convert text to lowercase in a Unicode-safe way.
            collapse_spaces: Whether to collapse multiple spaces into one.
            strip: Whether to trim leading/trailing spaces.
            unicode_form: Unicode normalization form (default: NFKC).

        Returns:
            Normalized string. If input is None, returns an empty string.
        """
        if s is None:
            return ""

        # Unicode normalization
        if unicode_form:
            s = unicodedata.normalize(unicode_form, s)

        # Case folding
        if apply_casefold:
            s = s.casefold()

        # Collapse multiple whitespaces
        if collapse_spaces:
            s = re.sub(r"\s+", " ", s)

        # Trim leading/trailing spaces
        if strip:
            s = s.strip()

        return s
