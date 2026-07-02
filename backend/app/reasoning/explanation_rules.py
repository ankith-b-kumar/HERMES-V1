from app.reasoning.evidence_collector import Evidence
from app.reasoning.explanation_schema import EXPLANATION_SCHEMA
from app.reasoning.explanation_types import ExplanationType
from app.reasoning.filtered_evidence import FilteredEvidence


class ExplanationRules:
    """
    Applies configuration-driven explanation rules.

    Converts raw evidence into recruiter-facing
    highlights and concerns based on configurable
    thresholds.
    """

    def apply(
        self,
        evidence: Evidence,
    ) -> FilteredEvidence:

        fv = evidence.feature_vector

        filtered = FilteredEvidence()

        for feature_name, rule in EXPLANATION_SCHEMA.items():

            value = getattr(fv, feature_name)

            threshold = rule["threshold"]
            message = rule["message"]
            rule_type = rule["type"]

            if value < threshold:
                continue

            if rule_type == ExplanationType.HIGHLIGHT:

                filtered.highlights.append(message)

            elif rule_type == ExplanationType.CONCERN:

                filtered.concerns.append(message)

        return filtered