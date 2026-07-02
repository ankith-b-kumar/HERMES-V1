from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class FinalCandidateResult:
    """
    Final output of the HERMES pipeline.

    Produced after both ranking and reasoning are complete.
    This is the canonical object consumed by the submission layer.
    """

    candidate_id: str

    final_score: float

    reasoning: str

    explanations: list[str] = field(default_factory=list)

    highlights: list[str] = field(default_factory=list)

    concerns: list[str] = field(default_factory=list)