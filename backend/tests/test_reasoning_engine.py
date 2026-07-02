from app.features.feature_vector import FeatureVector
from app.ranking.ranking_result import RankingResult
from app.reasoning.reasoning_engine import ReasoningEngine


def test_reasoning_engine():

    fv = FeatureVector(
        candidate_id="1",
        required_skill_match=1.0,
        years_experience_score=1.0,
        project_relevance_score=1.0,
        trust_score=1.0,
    )

    ranking = RankingResult(
        candidate_id="1",
        final_score=0.95,
        base_score=0.93,
        risk_penalty=0.02,
        behavior_bonus=0.04,
    )

    engine = ReasoningEngine()

    explanation, text = engine.explain(
        fv,
        ranking,
    )

    assert explanation.summary.startswith("Excellent")
    assert "Strengths:" in text