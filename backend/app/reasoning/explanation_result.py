from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class ExplanationResult:
    """
    Human-readable explanation accompanying a ranked candidate.
    """

    candidate_id: str

    final_score: float

    summary: str

    highlights: list[str] = field(default_factory=list)

    concerns: list[str] = field(default_factory=list)