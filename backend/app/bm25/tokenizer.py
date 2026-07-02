import re


class Tokenizer:
    """
    Shared tokenizer for lexical retrieval.
    """

    TOKEN_PATTERN = re.compile(r"[a-z0-9+#.]+")

    def tokenize(self, text: str) -> list[str]:
        """
        Convert normalized text into searchable tokens.
        """

        return self.TOKEN_PATTERN.findall(text.lower())