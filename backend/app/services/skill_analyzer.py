from app.models.candidate import Candidate
from app.models.job_profile import JobProfile
from app.models.skill_profile import SkillProfile
from app.services.knowledge_service import KnowledgeService


class SkillAnalyzer:
    """
    Extract skill evidence from a candidate
    relative to a Job Description.
    """

    def __init__(self):
        self.knowledge = KnowledgeService()

    def analyze(
        self,
        candidate: Candidate,
        job: JobProfile,
    ) -> SkillProfile:

        profile = SkillProfile()

        candidate_skills = {
            skill.lower()
            for skill in candidate.skills
        }

        required = {
            skill.lower()
            for skill in job.required_skills
        }

        profile.extracted_skills = sorted(candidate_skills)

        profile.matched_skills = sorted(
            candidate_skills & required
        )

        profile.missing_skills = sorted(
            required - candidate_skills
        )

        profile.total_skills = len(candidate_skills)

        categories = []

        for category, skills in self.knowledge.skills.items():

            if any(
                skill in candidate_skills
                for skill in skills
            ):
                categories.append(category)

        profile.skill_categories = sorted(categories)

        return profile