from app.features.feature_vector import FeatureVector
from app.ranking.ranking_result import RankingResult
from app.reasoning.evidence_collector import EvidenceCollector
from app.reasoning.explanation_builder import ExplanationBuilder
from app.reasoning.explanation_formatter import ExplanationFormatter
from app.reasoning.explanation_rules import ExplanationRules


class ReasoningEngine:

    def __init__(self):

        self.collector = EvidenceCollector()

        self.rules = ExplanationRules()

        self.builder = ExplanationBuilder()

        self.formatter = ExplanationFormatter()

    def explain(
        self,
        feature_vector: FeatureVector,
        ranking_result: RankingResult,
    ):

        evidence = self.collector.collect(
            feature_vector,
            ranking_result,
        )

        filtered = self.rules.apply(
            evidence
        )

        explanation = self.builder.build(
            ranking_result,
            filtered,
        )

        formatted = self.formatter.format(
            explanation
        )

        return explanation, formatted