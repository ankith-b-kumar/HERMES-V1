from app.features.feature_vector import FeatureVector


def test_feature_vector_defaults():
    fv = FeatureVector(candidate_id="123")

    assert fv.candidate_id == "123"
    assert fv.bm25_score == 0.0
    assert fv.embedding_score == 0.0
    assert fv.required_skill_match == 0.0
    assert fv.trust_score == 0.0
    assert fv.risk_score == 0.0
    assert fv.metadata == {}