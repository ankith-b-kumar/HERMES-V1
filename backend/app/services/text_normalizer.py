import re

from app.services.knowledge_service import KnowledgeService


class TextNormalizer:
    """
    Responsible for cleaning and normalizing text before extraction.
    """

    def __init__(self):
        self.knowledge = KnowledgeService()

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

        for short, full in self.knowledge.synonyms.items():

            pattern = r"\b" + re.escape(short.lower()) + r"\b"

            text = re.sub(
                pattern,
                full.lower(),
                text,
                flags=re.IGNORECASE,
            )

        return text