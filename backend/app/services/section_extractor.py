import re
from typing import Dict


class SectionExtractor:
    """
    Splits a Job Description into logical sections.
    """

    SECTION_HEADERS = [
        "required",
        "required skills",
        "requirements",
        "preferred",
        "preferred skills",
        "preferred qualifications",
        "nice to have",
        "education",
        "experience",
        "responsibilities",
        "qualifications",
        "skills"
    ]

    def extract(self, text: str) -> Dict[str, str]:

        sections = {}

        current = "general"

        sections[current] = []

        lines = text.splitlines()

        for line in lines:

            cleaned = line.strip().lower()

            if not cleaned:
                continue

            matched = False

            for header in self.SECTION_HEADERS:

                if cleaned.startswith(header):

                    current = header

                    sections.setdefault(current, [])

                    matched = True

                    break

            if not matched:

                sections.setdefault(current, []).append(cleaned)

        return {
            key: "\n".join(value)
            for key, value in sections.items()
        }