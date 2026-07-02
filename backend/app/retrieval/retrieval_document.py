from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RetrievalDocument:
    """
    Canonical searchable representation of a candidate.
    """

    candidate_id: str

    text: str

    sections: dict[str, str]

    token_count: int