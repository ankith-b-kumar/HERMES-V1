import re


class ExperienceExtractor:
    """
    Extract minimum years of experience.
    """

    def extract(self, text: str) -> float:

        match = re.search(
            r"(\d+)\+?\s*(?:years?|yrs?)",
            text,
            flags=re.IGNORECASE,
        )

        if match:
            return float(match.group(1))

        return 0.0