from app.ranking.aggregated_feature_scores import AggregatedFeatureScores
from app.ranking.score_fusion import ScoreFusion


def test_score_fusion_perfect_candidate():

    scores = AggregatedFeatureScores(
        retrieval=1,
        skills=1,
        experience=1,
        projects=1,
        education=1,
        company=1,
        behavior=1,
        trust=1,
    )

    fusion = ScoreFusion()

    score = fusion.compute(scores)

    assert abs(score - 1.0) < 1e-6