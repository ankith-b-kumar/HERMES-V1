from app.reasoning.explanation_result import ExplanationResult
from app.reasoning.explanation_templates import SUMMARY_TEMPLATES
from app.reasoning.filtered_evidence import FilteredEvidence
from app.ranking.ranking_result import RankingResult


class ExplanationBuilder:

    def build(
        self,
        ranking_result: RankingResult,
        filtered: FilteredEvidence,
    ) -> ExplanationResult:

        score = ranking_result.final_score

        if score >= 0.90:
            summary = SUMMARY_TEMPLATES["excellent"]

        elif score >= 0.75:
            summary = SUMMARY_TEMPLATES["strong"]

        elif score >= 0.50:
            summary = SUMMARY_TEMPLATES["moderate"]

        else:
            summary = SUMMARY_TEMPLATES["weak"]

        return ExplanationResult(
            candidate_id=ranking_result.candidate_id,
            final_score=ranking_result.final_score,
            summary=summary,
            highlights=filtered.highlights,
            concerns=filtered.concerns,
        )