from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class RankingResult:
    """
    Final ranking output for a candidate.
    """

    candidate_id: str

    final_score: float

    base_score: float

    risk_penalty: float

    behavior_bonus: float

    explanations: list[str] = field(default_factory=list)