from dataclasses import dataclass

from app.features.feature_vector import FeatureVector
from app.ranking.behavior_assessment import BehaviorAssessment
from app.ranking.risk_assessment import RiskAssessment


@dataclass(slots=True, frozen=True)
class RankingInput:
    """
    Complete input required by the Ranking Engine.

    Produced after the Feature Layer and Intelligence Agents
    have finished their work.
    """

    feature_vector: FeatureVector

    risk: RiskAssessment

    behavior: BehaviorAssessment