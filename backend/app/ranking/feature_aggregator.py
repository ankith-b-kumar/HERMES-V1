from app.features.feature_vector import FeatureVector
from app.ranking.aggregated_feature_scores import AggregatedFeatureScores


class FeatureAggregator:
    """
    Aggregates low-level features into higher-level category scores.
    """

    def aggregate(
        self,
        features: FeatureVector,
    ) -> AggregatedFeatureScores:

        retrieval = (
            features.bm25_score
            + features.embedding_score
            + features.ontology_score
            + features.rule_score
        ) / 4

        skills = (
            features.required_skill_match
            + features.preferred_skill_match
            + features.rare_skill_bonus
        ) / 3

        experience = (
            features.years_experience_score
            + features.role_similarity_score
        ) / 2

        behavior = (
            features.leadership_score
            + features.ownership_score
            + features.impact_score
            + features.communication_score
        ) / 4

        return AggregatedFeatureScores(
            retrieval=retrieval,
            skills=skills,
            experience=experience,
            projects=features.project_relevance_score,
            education=features.education_score,
            company=features.company_relevance_score,
            behavior=behavior,
            trust=features.trust_score,
        )