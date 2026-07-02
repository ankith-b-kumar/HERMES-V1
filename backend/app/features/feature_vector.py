from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class FeatureVector:
    """
    Canonical feature representation used by the Ranking Layer.

    Every score is normalized to [0.0, 1.0] unless otherwise noted.
    """

    candidate_id: str

    # -----------------------------
    # Retrieval Features
    # -----------------------------
    bm25_score: float = 0.0
    embedding_score: float = 0.0
    ontology_score: float = 0.0
    rule_score: float = 0.0

    # -----------------------------
    # Skill Features
    # -----------------------------
    required_skill_match: float = 0.0
    preferred_skill_match: float = 0.0
    rare_skill_bonus: float = 0.0

    # -----------------------------
    # Experience Features
    # -----------------------------
    years_experience_score: float = 0.0
    role_similarity_score: float = 0.0

    # -----------------------------
    # Project Features
    # -----------------------------
    project_relevance_score: float = 0.0

    # -----------------------------
    # Education Features
    # -----------------------------
    education_score: float = 0.0

    # -----------------------------
    # Company Features
    # -----------------------------
    company_relevance_score: float = 0.0

    # -----------------------------
    # Behavioral Features
    # -----------------------------
    leadership_score: float = 0.0
    ownership_score: float = 0.0
    impact_score: float = 0.0
    communication_score: float = 0.0

    # -----------------------------
    # Trust Features
    # -----------------------------
    trust_score: float = 0.0

    # -----------------------------
    # Risk Features
    # -----------------------------
    risk_score: float = 0.0

    # Optional diagnostic metadata
    metadata: Dict[str, float | str] = field(default_factory=dict)