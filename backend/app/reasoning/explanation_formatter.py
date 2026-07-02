from app.reasoning.explanation_result import ExplanationResult


class ExplanationFormatter:
    """
    Converts ExplanationResult into a readable string.
    """

    def format(
        self,
        explanation: ExplanationResult,
    ) -> str:

        lines = [
            explanation.summary,
            "",
        ]

        if explanation.highlights:
            lines.append("Strengths:")

            for item in explanation.highlights:
                lines.append(f"- {item}")

            lines.append("")

        if explanation.concerns:
            lines.append("Concerns:")

            for item in explanation.concerns:
                lines.append(f"- {item}")

        return "\n".join(lines)