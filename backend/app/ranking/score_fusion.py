from app.ranking.aggregated_feature_scores import AggregatedFeatureScores
from app.ranking.ranking_config import RankingWeights


class ScoreFusion:
    """
    Computes the weighted base score from aggregated feature groups.
    """

    def __init__(self, weights: RankingWeights | None = None):
        self.weights = weights or RankingWeights()

    def compute(
        self,
        scores: AggregatedFeatureScores,
    ) -> float:

        return (

            scores.retrieval * self.weights.retrieval

            + scores.skills * self.weights.skills

            + scores.experience * self.weights.experience

            + scores.projects * self.weights.projects

            + scores.education * self.weights.education

            + scores.company * self.weights.company

            + scores.behavior * self.weights.behavior

            + scores.trust * self.weights.trust

        )