import re
from typing import List

from app.services.knowledge_service import KnowledgeService


class RoleExtractor:
    """
    Extracts job roles from text.
    """

    def __init__(self):
        self.knowledge = KnowledgeService()

    def extract(self, text: str) -> List[str]:

        found = set()

        for roles in self.knowledge.roles.values():

            for role in roles:

                pattern = (
                    r"\b"
                    + re.escape(role)
                    + r"\b"
                )

                if re.search(
                    pattern,
                    text,
                    flags=re.IGNORECASE,
                ):
                    found.add(role)

        return sorted(found)