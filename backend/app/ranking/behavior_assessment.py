from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class BehaviorAssessment:
    """
    Structured representation of behavioral evaluation.

    score:
        Overall behavioral score in [0.0, 1.0].

    Individual attributes remain available for
    explainability and debugging.
    """

    score: float

    leadership: float

    ownership: float

    communication: float

    impact: float

    evidence: list[str] = field(default_factory=list)