"""
Configuration-driven explanation rules.

Each rule determines whether a feature should
appear as a recruiter-facing highlight or concern.
"""

from app.reasoning.explanation_types import ExplanationType


EXPLANATION_SCHEMA = {

    # --------------------------------------------------
    # Highlights
    # --------------------------------------------------

    "required_skill_match": {
        "threshold": 0.80,
        "message": "Strong required skill alignment.",
        "type": ExplanationType.HIGHLIGHT,
    },

    "years_experience_score": {
        "threshold": 0.80,
        "message": "Relevant professional experience.",
        "type": ExplanationType.HIGHLIGHT,
    },

    "project_relevance_score": {
        "threshold": 0.80,
        "message": "Highly relevant project portfolio.",
        "type": ExplanationType.HIGHLIGHT,
    },

    "trust_score": {
        "threshold": 0.80,
        "message": "High confidence in resume evidence.",
        "type": ExplanationType.HIGHLIGHT,
    },

    # --------------------------------------------------
    # Concerns
    # --------------------------------------------------

    "risk_score": {
        "threshold": 0.50,
        "message": "Candidate presents elevated risk signals.",
        "type": ExplanationType.CONCERN,
    },
}