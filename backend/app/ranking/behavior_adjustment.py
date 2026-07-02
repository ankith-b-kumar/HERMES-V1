from app.ranking.behavior_assessment import BehaviorAssessment
from app.ranking.ranking_config import RankingParameters


class BehaviorAdjustment:
    """
    Applies a bounded bonus based on behavioral quality.
    """

    def __init__(
        self,
        params: RankingParameters | None = None,
    ):
        self.params = params or RankingParameters()

    def apply(
        self,
        score: float,
        assessment: BehaviorAssessment,
    ) -> float:
        """
        Apply a proportional bonus.

        The bonus is capped to avoid overpowering
        technical qualifications.
        """

        bonus = (
            assessment.score
            * self.params.max_behavior_bonus
        )

        adjusted = score * (1.0 + bonus)

        return max(
            self.params.minimum_final_score,
            min(
                adjusted,
                self.params.maximum_final_score,
            ),
        )