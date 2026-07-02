from .conftest import make_feature_vector, make_ranking_input
from app.ranking.ranking_engine import RankingEngine


def test_perfect_candidate():

    fv = make_feature_vector(
        candidate_id="1",
    )

    engine = RankingEngine()

    ranking_input = make_ranking_input(fv)

    result = engine.rank(ranking_input)

    assert result.candidate_id == "1"
    assert result.final_score > 0.99
    assert result.final_score <= 1.0


def test_risk_penalty():

    engine = RankingEngine()

    low = make_feature_vector(
        risk_score=0.0,
    )

    high = make_feature_vector(
        candidate_id="2",
        risk_score=1.0,
    )

    low_input = make_ranking_input(low)
    high_input = make_ranking_input(high)

    assert (
        engine.rank(high_input).final_score
        < engine.rank(low_input).final_score
    )


def test_behavior_bonus():

    engine = RankingEngine()

    weak = make_feature_vector(
        leadership_score=0.0,
        ownership_score=0.0,
        communication_score=0.0,
        impact_score=0.0,
    )

    strong = make_feature_vector()

    weak_input = make_ranking_input(weak)
    strong_input = make_ranking_input(strong)

    assert (
        engine.rank(strong_input).final_score
        > engine.rank(weak_input).final_score
    )


def test_score_bounds():

    engine = RankingEngine()

    fv = make_feature_vector()

    result = engine.rank(
        make_ranking_input(fv)
    )

    assert 0.0 <= result.final_score <= 1.0


def test_deterministic():

    engine = RankingEngine()

    fv = make_feature_vector()

    ranking_input = make_ranking_input(fv)

    score1 = engine.rank(ranking_input).final_score
    score2 = engine.rank(ranking_input).final_score

    assert score1 == score2


def test_result_consistency():

    engine = RankingEngine()

    fv = make_feature_vector()

    result = engine.rank(
        make_ranking_input(fv)
    )

    assert result.base_score >= 0
    assert result.risk_penalty >= 0
    assert result.behavior_bonus >= 0
    assert 0.0 <= result.final_score <= 1.0