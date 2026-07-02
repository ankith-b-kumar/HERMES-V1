from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RankingWeights:
    """
    Relative importance of each feature group.

    The weights should sum to 1.0.
    """

    retrieval: float = 0.25
    skills: float = 0.25
    experience: float = 0.15
    projects: float = 0.08
    education: float = 0.05
    company: float = 0.05
    behavior: float = 0.10
    trust: float = 0.07


@dataclass(frozen=True, slots=True)
class RankingParameters:
    """
    Tunable ranking parameters.

    These are thresholds and penalties, not feature weights.
    """
    max_behavior_bonus: float = 0.05
    # Maximum penalty applied when risk_score == 1.0
    max_risk_penalty: float = 0.20

    # Candidates below this trust score can optionally be filtered
    minimum_trust_score: float = 0.30

    # Candidates below this required skill score can optionally be filtered
    minimum_skill_match: float = 0.40

    # Maximum final score after adjustments
    maximum_final_score: float = 1.00

    # Minimum possible score
    minimum_final_score: float = 0.00