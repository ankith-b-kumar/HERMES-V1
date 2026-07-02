from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator

from app.core.config import settings
from app.ingestion.candidate_mapper import CandidateMapper
from app.models.candidate import Candidate


class CandidateLoader:
    """
    Streams candidates from the JSONL dataset.
    """

    def __init__(
        self,
        dataset_path: Path | None = None,
    ):
        self.dataset_path = (
            dataset_path
            if dataset_path is not None
            else settings.DATASET_PATH
        )

        self.mapper = CandidateMapper()

    def load(self) -> Iterator[Candidate]:
        """
        Lazily load candidates one at a time.
        """

        with open(
            self.dataset_path,
            "r",
            encoding="utf-8",
        ) as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    record = json.loads(line)

                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON on line {line_number}"
                    ) from exc

                yield self.mapper.map(record)