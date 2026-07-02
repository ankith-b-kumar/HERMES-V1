from app.features.feature_vector import FeatureVector
from app.ranking.feature_aggregator import FeatureAggregator


def test_feature_aggregator():

    fv = FeatureVector(
        candidate_id="1",

        bm25_score=1,
        embedding_score=1,
        ontology_score=1,
        rule_score=1,

        required_skill_match=1,
        preferred_skill_match=1,
        rare_skill_bonus=1,

        years_experience_score=1,
        role_similarity_score=1,

        project_relevance_score=1,
        education_score=1,
        company_relevance_score=1,

        leadership_score=1,
        ownership_score=1,
        impact_score=1,
        communication_score=1,

        trust_score=1,
    )

    aggregator = FeatureAggregator()

    scores = aggregator.aggregate(fv)

    assert scores.retrieval == 1
    assert scores.skills == 1
    assert scores.experience == 1
    assert scores.behavior == 1
    assert scores.projects == 1
    assert scores.education == 1
    assert scores.company == 1
    assert scores.trust == 1