import re
from typing import List

from app.services.knowledge_service import KnowledgeService


class SkillExtractor:
    """
    Extracts skills from text using the shared knowledge base.
    """

    def __init__(self):
        self.knowledge = KnowledgeService()

    def extract(self, text: str) -> List[str]:

        found = set()

        for skill in self.knowledge.skill_index:

            pattern = (
                r"\b"
                + re.escape(skill)
                + r"\b"
            )

            if re.search(
                pattern,
                text,
                flags=re.IGNORECASE,
            ):
                found.add(skill)

        return sorted(found)