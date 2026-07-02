from dataclasses import dataclass, field
from typing import List


@dataclass
class JobProfile:
    """
    Structured representation of a Job Description.

    Produced by the JDAgent and consumed by all
    downstream intelligence agents.
    """

    # Role information
    role_titles: List[str] = field(default_factory=list)

    # Skills
    required_skills: List[str] = field(default_factory=list)
    preferred_skills: List[str] = field(default_factory=list)

    # Technologies / Tools
    tools: List[str] = field(default_factory=list)

    # Education
    education: List[str] = field(default_factory=list)

    # Certifications
    certifications: List[str] = field(default_factory=list)

    # Industry / Domain
    industries: List[str] = field(default_factory=list)

    # Generic keywords
    keywords: List[str] = field(default_factory=list)

    # Experience
    minimum_experience_years: float = 0.0