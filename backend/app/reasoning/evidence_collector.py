from dataclasses import dataclass

from app.features.feature_vector import FeatureVector
from app.ranking.ranking_result import RankingResult


@dataclass(slots=True)
class Evidence:
    """
    Raw evidence extracted from previous layers.

    Contains scores and assessments but no
    presentation logic.
    """

    feature_vector: FeatureVector

    ranking_result: RankingResult


class EvidenceCollector:
    """
    Collect raw evidence.

    No thresholds.
    No business rules.
    No presentation.
    """

    def collect(
        self,
        feature_vector: FeatureVector,
        ranking_result: RankingResult,
    ) -> Evidence:

        return Evidence(
            feature_vector=feature_vector,
            ranking_result=ranking_result,
        )