from types import SimpleNamespace

from app.features.feature_builder import FeatureBuilder
from app.features.feature_build_input import FeatureBuildInput


def test_feature_builder():

    candidate = SimpleNamespace(
        id="123",
        name="Alice",
    )

    retrieval = {
        "bm25": 20,
        "embedding": 0.91,
    }

    intelligence = {
        "required_skill_match": 0.95,
        "trust_score": 0.9,
        "risk_score": 0.2,
    }

    builder = FeatureBuilder()

    feature_input = FeatureBuildInput(
        candidate=candidate,
        retrieval_scores=retrieval,
        intelligence_scores=intelligence,
    )

    fv = builder.build(feature_input)

    assert fv.candidate_id == "123"

    # BM25 should be normalized (20 / 25 = 0.8)
    assert abs(fv.bm25_score - 0.8) < 1e-6

    assert abs(fv.embedding_score - 0.91) < 1e-6
    assert abs(fv.required_skill_match - 0.95) < 1e-6
    assert abs(fv.trust_score - 0.9) < 1e-6
    assert abs(fv.risk_score - 0.2) < 1e-6