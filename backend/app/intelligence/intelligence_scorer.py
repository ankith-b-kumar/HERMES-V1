"""
Converts intelligence profiles into normalized feature scores.

Each intelligence agent produces a structured profile.
This scorer converts those profiles into the numerical
feature values consumed by the FeatureBuilder.

Currently only skill-based scoring is implemented.
All other scores default to zero and can be extended later.
"""

from __future__ import annotations

from app.models.job_profile import JobProfile
from app.models.skill_profile import SkillProfile


DEFAULT_SCORES: dict[str, float] = {
    "required_skill_match": 0.0,
    "preferred_skill_match": 0.0,
    "rare_skill_bonus": 0.0,
    "years_experience_score": 0.0,
    "role_similarity_score": 0.0,
    "project_relevance_score": 0.0,
    "education_score": 0.0,
    "company_relevance_score": 0.0,
    "leadership_score": 0.0,
    "ownership_score": 0.0,
    "impact_score": 0.0,
    "communication_score": 0.0,
    "trust_score": 0.0,
    "risk_score": 0.0,
}


class IntelligenceScorer:
    """
    Converts intelligence profiles into normalized feature scores.
    """

    def score(
        self,
        profiles: dict,
        job_profile: JobProfile,
    ) -> dict[str, float]:

        scores = DEFAULT_SCORES.copy()

        skill_profile: SkillProfile | None = profiles.get("skill")

        if skill_profile is not None:

            required = max(
                len(job_profile.required_skills),
                1,
            )

            scores["required_skill_match"] = min(
                len(skill_profile.matched_skills) / required,
                1.0,
            )

            preferred = max(
                len(job_profile.preferred_skills),
                1,
            )

            preferred_matches = sum(
                1
                for skill in skill_profile.matched_skills
                if skill in job_profile.preferred_skills
            )

            scores["preferred_skill_match"] = min(
                preferred_matches / preferred,
                1.0,
            )

            scores["rare_skill_bonus"] = min(
                len(skill_profile.skill_categories) * 0.05,
                1.0,
            )

        return scores