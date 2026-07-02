from types import SimpleNamespace

from app.features.feature_extractor import FeatureExtractor


def test_feature_extractor():

    candidate = SimpleNamespace(
        id="1",
        name="Alice",
    )

    retrieval = {
        "bm25": 0.8,
        "embedding": 0.9,
        "ontology": 0.7,
        "rules": 0.6,
    }

    intelligence = {
        "required_skill_match": 0.95,
        "trust_score": 0.9,
        "risk_score": 0.1,
    }

    extractor = FeatureExtractor()

    fv = extractor.extract(
        candidate=candidate,
        retrieval_scores=retrieval,
        intelligence_scores=intelligence,
    )

    assert fv.candidate_id == "1"
    assert fv.bm25_score == 0.8
    assert fv.embedding_score == 0.9
    assert fv.required_skill_match == 0.95
    assert fv.trust_score == 0.9
    assert fv.risk_score == 0.1