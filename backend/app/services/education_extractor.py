import re
from typing import List

from app.services.knowledge_service import KnowledgeService


class EducationExtractor:
    """
    Extracts education requirements.
    """

    def __init__(self):
        self.knowledge = KnowledgeService()

    def extract(self, text: str) -> List[str]:

        found = set()

        for degree in self.knowledge.education["degrees"]:

            pattern = (
                r"\b"
                + re.escape(degree)
                + r"\b"
            )

            if re.search(
                pattern,
                text,
                flags=re.IGNORECASE,
            ):
                found.add(degree)

        return sorted(found)