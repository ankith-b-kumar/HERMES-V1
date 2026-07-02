from dataclasses import dataclass, field
from typing import List


@dataclass
class SkillProfile:
    """
    Structured skill evidence extracted from a candidate.
    """

    extracted_skills: List[str] = field(default_factory=list)

    matched_skills: List[str] = field(default_factory=list)

    missing_skills: List[str] = field(default_factory=list)

    skill_categories: List[str] = field(default_factory=list)

    total_skills: int = 0