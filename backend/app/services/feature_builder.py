from app.models.career_profile import CareerProfile
from app.models.feature_vector import FeatureVector
from app.models.job_profile import JobProfile
from app.models.skill_profile import SkillProfile


class FeatureBuilder:
    """
    Converts evidence from intelligence agents into
    a numerical feature vector.
    """

    def build(
        self,
        job: JobProfile,
        career: CareerProfile,
        skills: SkillProfile,
    ) -> FeatureVector:

        vector = FeatureVector()

        # Career
        vector.experience_years = career.total_experience_years

        # Skills
        vector.total_skills = skills.total_skills

        vector.matched_skills = len(
            skills.matched_skills
        )

        vector.missing_skills = len(
            skills.missing_skills
        )

        if job.required_skills:

            vector.required_skill_match_ratio = (
                len(skills.matched_skills)
                /
                len(job.required_skills)
            )

        return vector