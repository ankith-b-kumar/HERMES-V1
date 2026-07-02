from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AggregatedFeatureScores:
    """
    Aggregated feature groups used for score fusion.

    Every value is expected to be normalized to [0, 1].
    """

    retrieval: float
    skills: float
    experience: float
    projects: float
    education: float
    company: float
    behavior: float
    trust: float