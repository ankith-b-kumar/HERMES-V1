import re

from app.services.knowledge_service import KnowledgeService


class TextNormalizer:
    """
    Responsible for cleaning and normalizing text before extraction.
    """

    def __init__(self):
        self.knowledge = KnowledgeService()

        # Compile synonym regex patterns once
        self._compiled_synonyms = [
            (
                re.compile(
                    r"\b" + re.escape(short.lower()) + r"\b",
                    re.IGNORECASE,
                ),
                full.lower(),
            )
            for short, full in self.knowledge.synonyms.items()
        ]

    def normalize(self, text: str) -> str:
        """
        Normalize text while preserving line structure and
        expanding known synonyms.
        """

        text = text.lower()

        cleaned_lines = []

        for line in text.splitlines():

            line = re.sub(r"\s+", " ", line).strip()

            if line:
                cleaned_lines.append(line)

        text = "\n".join(cleaned_lines)

        for pattern, replacement in self._compiled_synonyms:
            text = pattern.sub(replacement, text)

        return text