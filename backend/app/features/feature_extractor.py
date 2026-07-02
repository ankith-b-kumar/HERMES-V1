from app.features.feature_vector import FeatureVector


class FeatureExtractor:
    """
    Collects outputs from retrieval and intelligence modules
    and converts them into a canonical FeatureVector.

    The extractor does not compute features—it only assembles them.
    """

    def extract(
        self,
        *,
        candidate,
        retrieval_scores: dict,
        intelligence_scores: dict,
    ) -> FeatureVector:

        return FeatureVector(

            candidate_id=candidate.id,

            # -------------------------
            # Retrieval
            # -------------------------

            bm25_score=retrieval_scores.get("bm25", 0.0),

            embedding_score=retrieval_scores.get("embedding", 0.0),

            ontology_score=retrieval_scores.get("ontology", 0.0),

            rule_score=retrieval_scores.get("rules", 0.0),

            # -------------------------
            # Skills
            # -------------------------

            required_skill_match=intelligence_scores.get(
                "required_skill_match", 0.0
            ),

            preferred_skill_match=intelligence_scores.get(
                "preferred_skill_match", 0.0
            ),

            rare_skill_bonus=intelligence_scores.get(
                "rare_skill_bonus", 0.0
            ),

            # -------------------------
            # Experience
            # -------------------------

            years_experience_score=intelligence_scores.get(
                "years_experience_score", 0.0
            ),

            role_similarity_score=intelligence_scores.get(
                "role_similarity_score", 0.0
            ),

            # -------------------------
            # Projects
            # -------------------------

            project_relevance_score=intelligence_scores.get(
                "project_relevance_score", 0.0
            ),

            # -------------------------
            # Education
            # -------------------------

            education_score=intelligence_scores.get(
                "education_score", 0.0
            ),

            # -------------------------
            # Company
            # -------------------------

            company_relevance_score=intelligence_scores.get(
                "company_relevance_score", 0.0
            ),

            # -------------------------
            # Behavioral
            # -------------------------

            leadership_score=intelligence_scores.get(
                "leadership_score", 0.0
            ),

            ownership_score=intelligence_scores.get(
                "ownership_score", 0.0
            ),

            impact_score=intelligence_scores.get(
                "impact_score", 0.0
            ),

            communication_score=intelligence_scores.get(
                "communication_score", 0.0
            ),

            # -------------------------
            # Trust
            # -------------------------

            trust_score=intelligence_scores.get(
                "trust_score", 0.0
            ),

            # -------------------------
            # Risk
            # -------------------------

            risk_score=intelligence_scores.get(
                "risk_score", 0.0
            ),

            metadata={
                "candidate_name": candidate.name
            }
        )