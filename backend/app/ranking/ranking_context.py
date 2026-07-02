from dataclasses import dataclass

from app.ranking.ranking_input import RankingInput

from app.features.feature_vector import FeatureVector
from app.ranking.aggregated_feature_scores import (
    AggregatedFeatureScores,
)
from app.ranking.behavior_assessment import (
    BehaviorAssessment,
)
from app.ranking.risk_assessment import (
    RiskAssessment,
)


@dataclass(slots=True)
class RankingContext:
    """
    Shared state passed through the ranking pipeline.

    Every ranking stage updates this context.
    """

    ranking_input: RankingInput

    aggregated_scores: AggregatedFeatureScores | None = None

    base_score: float = 0.0

    adjusted_score: float = 0.0

    final_score: float = 0.0