from typing import Any, Dict

from app.agents.base_agent import BaseAgent
from app.agents.career_agent import CareerAgent
from app.agents.jd_agent import JDAgent
from app.agents.skill_agent import SkillAgent
from app.services.feature_builder import FeatureBuilder


class Orchestrator(BaseAgent):
    """
    Coordinates all HERMES intelligence agents.

    The orchestrator contains NO business logic.
    It only controls workflow.
    """

    def __init__(self):
        super().__init__("Orchestrator")

        # Intelligence Agents
        self.jd_agent = JDAgent()
        self.career_agent = CareerAgent()
        self.skill_agent = SkillAgent()
        self.feature_builder = FeatureBuilder()

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the intelligence pipeline.

        Expected input:
        {
            "job_description": "...",
            "candidate": Candidate(...)
        }
        """

        self.logger.info("Starting HERMES workflow")

        candidate = input_data["candidate"]
        job_description = input_data["job_description"]

        # Step 1
        job_profile = self.jd_agent.run(job_description)

        # Step 2
        career_profile = self.career_agent.run(candidate)

        # Step 3
        skill_profile = self.skill_agent.run(
            (candidate, job_profile)
        )
        
        feature_vector = self.feature_builder.build(
            job_profile,
            career_profile,
            skill_profile,
        )

        self.logger.info("Workflow completed")

        return {
            "job_profile": job_profile,
            "career_profile": career_profile,
            "skill_profile": skill_profile,
            "feature_vector": feature_vector,
        }