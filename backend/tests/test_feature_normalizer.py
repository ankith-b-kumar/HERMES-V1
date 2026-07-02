from app.features.feature_normalizer import FeatureNormalizer
from app.features.feature_vector import FeatureVector


def test_feature_normalizer():

    fv = FeatureVector(
        candidate_id="1",
        bm25_score=30,
        embedding_score=1.2,
        trust_score=2,
        risk_score=-1,
    )

    normalizer = FeatureNormalizer()

    normalized = normalizer.normalize(fv)

    assert normalized.bm25_score == 1.0
    assert normalized.embedding_score == 1.0
    assert normalized.trust_score == 1.0
    assert normalized.risk_score == 0.0

    # Original object should remain unchanged
    assert fv.bm25_score == 30