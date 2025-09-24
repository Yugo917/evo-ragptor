from typing import List


class TextChunker:
    """
    Utility class to split long texts into word-level chunks of approximately
    `chunk_size` words. This helps models with token length limits (e.g., 512 tokens).
    """
    def __init__(self, chunk_size: int = 256) -> None:
        self.chunk_size = max(1, int(chunk_size))

    def chunk(self, text: str) -> List[str]:
        """
        Split text into chunks of ~`chunk_size` words.

        Notes:
        - Works on whitespace-delimited words (simple and fast).
        - If the text is empty, returns [""] to keep downstream shapes consistent.
        """
        if not text:
            return [""]
        words = text.split()
        if len(words) <= self.chunk_size:
            return [" ".join(words)]
        return [
            " ".join(words[i:i + self.chunk_size])
            for i in range(0, len(words), self.chunk_size)
        ]
