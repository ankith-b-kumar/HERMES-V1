"""
CSV writer for Redrob Hackathon submissions.

This module is responsible only for serializing already-ranked
submission rows into the official CSV format.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from app.submission.submission_models import SubmissionRow

MAX_SUBMISSION_ROWS = 100

CSV_HEADER = [
    "candidate_id",
    "rank",
    "score",
    "reasoning",
]


class CSVWriter:
    """
    Writes the official submission CSV.

    Ordering is deterministic:

        1. score (descending)
        2. candidate_id (ascending)

    This satisfies the official tie-breaking requirement.
    """

    def write(
        self,
        rows: Iterable[SubmissionRow],
        output_path: str | Path,
    ) -> Path:

        output_path = Path(output_path)

        rows = list(rows)

        if len(rows) != MAX_SUBMISSION_ROWS:
            raise ValueError(
                f"Expected exactly {MAX_SUBMISSION_ROWS} submission rows, "
                f"received {len(rows)}."
            )

        rows.sort(
            key=lambda row: (
                -row.score,
                row.candidate_id,
            )
        )

        with output_path.open(
            mode="w",
            encoding="utf-8",
            newline="",
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(CSV_HEADER)

            for rank, row in enumerate(rows, start=1):

                if not row.candidate_id:
                    raise ValueError("candidate_id cannot be empty.")

                if not isinstance(row.score, (int, float)):
                    raise TypeError("score must be numeric.")

                writer.writerow(
                    [
                        row.candidate_id,
                        rank,
                        f"{row.score:.6f}",
                        row.reasoning,
                    ]
                )

        return output_path