from app.ranking.ranking_config import RankingWeights
from app.ranking.ranking_config import (
    RankingParameters,
    RankingWeights,
)



def test_weights_sum_to_one():

    weights = RankingWeights()

    total = (
        weights.retrieval
        + weights.skills
        + weights.experience
        + weights.projects
        + weights.education
        + weights.company
        + weights.behavior
        + weights.trust
    )

    assert abs(total - 1.0) < 1e-6
    
def test_ranking_parameters_defaults():

    params = RankingParameters()

    assert params.max_risk_penalty == 0.20
    assert params.minimum_trust_score == 0.30
    assert params.minimum_skill_match == 0.40
    assert params.maximum_final_score == 1.00
    assert params.minimum_final_score == 0.00