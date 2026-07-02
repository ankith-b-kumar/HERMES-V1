"""
Coordinates all intelligence agents.

Produces structured intelligence profiles that can later
be converted into feature scores.
"""

from __future__ import annotations

from app.agents.behavior_agent import BehaviorAgent
from app.agents.career_agent import CareerAgent
from app.agents.company_agent import CompanyAgent
from app.agents.project_agent import ProjectAgent
from app.agents.risk_agent import RiskAgent
from app.agents.skill_agent import SkillAgent
from app.agents.trust_agent import TrustAgent


class IntelligenceEngine:
    """
    Executes all intelligence agents.
    """

    def __init__(self):

        self.skill = SkillAgent()
        self.career = CareerAgent()
        self.project = ProjectAgent()
        self.company = CompanyAgent()
        self.behavior = BehaviorAgent()
        self.trust = TrustAgent()
        self.risk = RiskAgent()

    def analyze(
        self,
        candidate,
        job_profile,
    ) -> dict:

        return {
            "skill": self.skill.run((candidate, job_profile)),
            "career": self.career.run((candidate, job_profile)),
            "project": self.project.run((candidate, job_profile)),
            "company": self.company.run((candidate, job_profile)),
            "behavior": self.behavior.run((candidate, job_profile)),
            "trust": self.trust.run((candidate, job_profile)),
            "risk": self.risk.run((candidate, job_profile)),
        }