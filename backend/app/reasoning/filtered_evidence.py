from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class FilteredEvidence:
    """
    Evidence selected for presentation.

    Only contains recruiter-facing highlights
    and concerns.
    """

    highlights: list[str] = field(default_factory=list)

    concerns: list[str] = field(default_factory=list)