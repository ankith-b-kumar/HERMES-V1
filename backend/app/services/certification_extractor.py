import re
from typing import List

from app.services.knowledge_service import KnowledgeService


class CertificationExtractor:
    """
    Extract certifications.
    """

    def __init__(self):
        self.knowledge = KnowledgeService()

    def extract(self, text: str) -> List[str]:

        found = set()

        for certs in self.knowledge.certifications.values():

            for cert in certs:

                pattern = (
                    r"\b"
                    + re.escape(cert)
                    + r"\b"
                )

                if re.search(
                    pattern,
                    text,
                    flags=re.IGNORECASE,
                ):
                    found.add(cert)

        return sorted(found)