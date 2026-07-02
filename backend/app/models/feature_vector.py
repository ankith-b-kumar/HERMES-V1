from dataclasses import dataclass


@dataclass
class FeatureVector:
    """
    Unified numerical representation of a candidate
    for the ranking engine.
    """

    experience_years: float = 0.0

    total_skills: int = 0

    matched_skills: int = 0

    missing_skills: int = 0

    required_skill_match_ratio: float = 0.0

    education_match: float = 0.0

    certification_match: float = 0.0

    role_match: float = 0.0