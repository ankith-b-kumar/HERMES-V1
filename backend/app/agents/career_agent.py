from typing import Any

from app.agents.base_agent import BaseAgent
from app.models.career_profile import CareerProfile
from app.services.career_analyzer import CareerAnalyzer


class CareerAgent(BaseAgent):
    """
    Intelligence agent responsible for
    understanding a candidate's career.
    """

    def __init__(self):
        super().__init__("CareerAgent")
        self.analyzer = CareerAnalyzer()

    def run(self, input_data: Any) -> CareerProfile:

        self.logger.info(
            "Analyzing candidate career..."
        )

        return self.analyzer.analyze(input_data)