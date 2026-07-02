import re
from typing import List

from app.models.job_profile import JobProfile

from app.services.text_normalizer import TextNormalizer
from app.services.section_extractor import SectionExtractor

from app.services.skill_extractor import SkillExtractor
from app.services.role_extractor import RoleExtractor
from app.services.education_extractor import EducationExtractor
from app.services.certification_extractor import CertificationExtractor
from app.services.experience_extractor import ExperienceExtractor

from app.services.knowledge_service import KnowledgeService


class JDParser:
    """
    Coordinates Job Description parsing.

    This class contains almost no parsing logic.
    It orchestrates specialized extractors.
    """

    def __init__(self):

        self.knowledge = KnowledgeService()

        self.normalizer = TextNormalizer()

        self.section_extractor = SectionExtractor()

        self.skill_extractor = SkillExtractor()

        self.role_extractor = RoleExtractor()

        self.education_extractor = EducationExtractor()

        self.certification_extractor = CertificationExtractor()

        self.experience_extractor = ExperienceExtractor()

    def parse(self, jd_text: str) -> JobProfile:

        normalized = self.normalizer.normalize(jd_text)

        sections = self.section_extractor.extract(normalized)

        profile = JobProfile()

        required_text = (
            sections.get("required skills")
            or sections.get("requirements")
            or sections.get("required")
            or normalized
        )

        preferred_text = (
            sections.get("preferred skills")
            or sections.get("preferred qualifications")
            or sections.get("preferred")
            or sections.get("nice to have")
            or ""
        )

        profile.required_skills = (
            self.skill_extractor.extract(required_text)
        )

        profile.preferred_skills = (
            self.skill_extractor.extract(preferred_text)
        )

        profile.role_titles = (
            self.role_extractor.extract(normalized)
        )

        profile.education = (
            self.education_extractor.extract(normalized)
        )

        profile.certifications = (
            self.certification_extractor.extract(normalized)
        )

        profile.industries = (
            self.extract_industries(normalized)
        )

        profile.keywords = (
            self.extract_keywords(normalized)
        )

        profile.minimum_experience_years = (
            self.experience_extractor.extract(normalized)
        )

        return profile

    # --------------------------------------------------
    # Industry Extraction
    # --------------------------------------------------

    def extract_industries(self, text: str) -> List[str]:

        found = set()

        for industry in self.knowledge.industries["domains"]:

            pattern = r"\b" + re.escape(industry) + r"\b"

            if re.search(pattern, text, re.IGNORECASE):
                found.add(industry)

        return sorted(found)

    # --------------------------------------------------
    # Keyword Extraction
    # --------------------------------------------------

    def extract_keywords(self, text: str) -> List[str]:

        words = re.findall(
            r"\b[a-zA-Z][a-zA-Z0-9+#.-]*\b",
            text,
        )

        stopwords = {
            "the",
            "and",
            "or",
            "to",
            "of",
            "for",
            "with",
            "in",
            "on",
            "a",
            "an",
            "is",
            "are",
            "be",
            "as",
            "at",
            "by",
            "from",
        }

        return sorted(
            {
                word
                for word in words
                if word not in stopwords
            }
        )