"""
Defines how each feature should be normalized.

The schema is intentionally data-only.
No business logic belongs here.
"""

FEATURE_SCHEMA = {

    # -------------------------
    # Retrieval Features
    # -------------------------

    "bm25_score": {
        "method": "min_max",
        "min": 0.0,
        "max": 25.0,
    },

    "embedding_score": {
        "method": "clip",
    },

    "ontology_score": {
        "method": "clip",
    },

    "rule_score": {
        "method": "clip",
    },

    # -------------------------
    # Skill Features
    # -------------------------

    "required_skill_match": {
        "method": "clip",
    },

    "preferred_skill_match": {
        "method": "clip",
    },

    "rare_skill_bonus": {
        "method": "clip",
    },

    # -------------------------
    # Experience
    # -------------------------

    "years_experience_score": {
        "method": "clip",
    },

    "role_similarity_score": {
        "method": "clip",
    },

    # -------------------------
    # Projects
    # -------------------------

    "project_relevance_score": {
        "method": "clip",
    },

    # -------------------------
    # Education
    # -------------------------

    "education_score": {
        "method": "clip",
    },

    # -------------------------
    # Company
    # -------------------------

    "company_relevance_score": {
        "method": "clip",
    },

    # -------------------------
    # Behavioral
    # -------------------------

    "leadership_score": {
        "method": "clip",
    },

    "ownership_score": {
        "method": "clip",
    },

    "impact_score": {
        "method": "clip",
    },

    "communication_score": {
        "method": "clip",
    },

    # -------------------------
    # Trust / Risk
    # -------------------------

    "trust_score": {
        "method": "clip",
    },

    "risk_score": {
        "method": "clip",
    },
}