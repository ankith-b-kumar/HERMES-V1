from app.ranking.behavior_adjustment import BehaviorAdjustment
from app.ranking.feature_aggregator import FeatureAggregator
from app.ranking.ranking_context import RankingContext
from app.ranking.ranking_input import RankingInput
from app.ranking.ranking_result import RankingResult
from app.ranking.risk_adjustment import RiskAdjustment
from app.ranking.score_fusion import ScoreFusion


class RankingEngine:
    """
    End-to-end ranking engine.

    Pipeline:

    RankingInput
        ↓
    FeatureAggregator
        ↓
    ScoreFusion
        ↓
    RiskAdjustment
        ↓
    BehaviorAdjustment
        ↓
    RankingResult
    """

    def __init__(self):
        self.aggregator = FeatureAggregator()
        self.fusion = ScoreFusion()
        self.risk = RiskAdjustment()
        self.behavior = BehaviorAdjustment()

    def rank(
        self,
        ranking_input: RankingInput,
    ) -> RankingResult:
        """
        Rank a candidate using precomputed feature and assessment data.
        """

        context = RankingContext(
            ranking_input=ranking_input
        )

        # Single source of truth
        fv = context.ranking_input.feature_vector
        risk = context.ranking_input.risk
        behavior = context.ranking_input.behavior

        # Aggregate feature groups
        context.aggregated_scores = self.aggregator.aggregate(fv)

        # Compute weighted base score
        context.base_score = self.fusion.compute(
            context.aggregated_scores
        )

        # Apply risk penalty
        context.adjusted_score = self.risk.apply(
            context.base_score,
            risk,
        )

        # Apply behavior bonus
        context.final_score = self.behavior.apply(
            context.adjusted_score,
            behavior,
        )

        risk_penalty = (
            context.base_score
            - context.adjusted_score
        )

        behavior_bonus = (
            context.final_score
            - context.adjusted_score
        )

        return RankingResult(
            candidate_id=fv.candidate_id,
            final_score=context.final_score,
            base_score=context.base_score,
            risk_penalty=risk_penalty,
            behavior_bonus=behavior_bonus,
        )