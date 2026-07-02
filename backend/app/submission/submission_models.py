from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SubmissionRow:
    """
    Canonical CSV row.
    """

    candidate_id: str

    score: float

    reasoning: str