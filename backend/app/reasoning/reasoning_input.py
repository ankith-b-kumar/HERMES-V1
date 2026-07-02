from dataclasses import dataclass

from app.models.job_profile import JobProfile
from app.ranking.ranking_result import RankingResult


@dataclass(slots=True, frozen=True)
class ReasoningInput:
    """
    Input to the ReasoningEngine.
    """

    job_profile: JobProfile

    ranking_results: list[RankingResult]