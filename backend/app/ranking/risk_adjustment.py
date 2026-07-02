from app.ranking.ranking_config import RankingParameters
from app.ranking.risk_assessment import RiskAssessment


class RiskAdjustment:
    """
    Applies a bounded proportional penalty based on
    candidate risk assessment.
    """

    def __init__(
        self,
        params: RankingParameters | None = None,
    ):
        self.params = params or RankingParameters()

    def apply(
        self,
        base_score: float,
        assessment: RiskAssessment,
    ) -> float:

        penalty = (
            assessment.score
            * self.params.max_risk_penalty
        )

        adjusted = base_score * (1.0 - penalty)

        return max(
            self.params.minimum_final_score,
            min(
                adjusted,
                self.params.maximum_final_score,
            ),
        )