from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class RiskAssessment:
    """
    Structured representation of candidate risk.

    score:
        Normalized risk score in [0.0, 1.0]

    reasons:
        Human-readable explanations describing why the
        candidate received this risk score.
    """

    score: float

    reasons: list[str] = field(default_factory=list)