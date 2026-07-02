from typing import Any

from app.agents.base_agent import BaseAgent
from app.models.skill_profile import SkillProfile
from app.services.skill_analyzer import SkillAnalyzer


class SkillAgent(BaseAgent):
    """
    Intelligence agent responsible for
    skill analysis.
    """

    def __init__(self):
        super().__init__("SkillAgent")
        self.analyzer = SkillAnalyzer()

    def run(self, input_data: Any) -> SkillProfile:

        candidate, job_profile = input_data

        self.logger.info(
            "Analyzing candidate skills..."
        )

        return self.analyzer.analyze(
            candidate,
            job_profile,
        )