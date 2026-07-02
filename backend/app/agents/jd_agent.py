from typing import Any

from app.agents.base_agent import BaseAgent
from app.models.job_profile import JobProfile
from app.services.jd_parser import JDParser


class JDAgent(BaseAgent):
    """
    Intelligence Agent responsible for understanding
    a Job Description.
    """

    def __init__(self):
        super().__init__("JDAgent")
        self.parser = JDParser()

    def run(self, input_data: Any) -> JobProfile:

        if not isinstance(input_data, str):
            raise ValueError("Job Description must be a string.")

        self.logger.info("Starting JD parsing.")

        profile = self.parser.parse(input_data)

        self.logger.info(
            "JD parsing completed successfully."
        )

        return profile