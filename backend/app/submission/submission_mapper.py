from app.submission.final_candidate_result import FinalCandidateResult
from app.submission.submission_models import SubmissionRow


class SubmissionMapper:
    """
    Converts pipeline output into CSV rows.
    """

    def map(
        self,
        results: list[FinalCandidateResult],
    ) -> list[SubmissionRow]:

        return [
            SubmissionRow(
                candidate_id=result.candidate_id,
                score=result.final_score,
                reasoning=result.reasoning,
            )
            for result in results
        ]