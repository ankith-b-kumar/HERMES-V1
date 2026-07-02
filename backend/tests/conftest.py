from app.features.feature_vector import FeatureVector

from app.ranking.behavior_assessment import BehaviorAssessment
from app.ranking.ranking_input import RankingInput
from app.ranking.risk_assessment import RiskAssessment


def make_ranking_input(feature_vector):
    """
    Build a RankingInput for tests from a FeatureVector.
    """

    behavior_score = (
        feature_vector.leadership_score
        + feature_vector.ownership_score
        + feature_vector.communication_score
        + feature_vector.impact_score
    ) / 4

    return RankingInput(
        feature_vector=feature_vector,
        risk=RiskAssessment(
            score=feature_vector.risk_score,
        ),
        behavior=BehaviorAssessment(
            score=behavior_score,
            leadership=feature_vector.leadership_score,
            ownership=feature_vector.ownership_score,
            communication=feature_vector.communication_score,
            impact=feature_vector.impact_score,
        ),
    )


def make_feature_vector(**overrides):

    defaults = dict(

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
        communication_score=1,
        impact_score=1,

        trust_score=1,

        risk_score=0,
    )

    defaults.update(overrides)

    return FeatureVector(**defaults)