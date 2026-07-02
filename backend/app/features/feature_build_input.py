from dataclasses import dataclass

from app.models.candidate import Candidate


@dataclass(slots=True, frozen=True)
class FeatureBuildInput:
    """
    Input object for the FeatureBuilder.

    Encapsulates all information required to construct
    a normalized FeatureVector for a single candidate.
    """

    candidate: Candidate

    retrieval_scores: dict[str, float]

    intelligence_scores: dict[str, float]