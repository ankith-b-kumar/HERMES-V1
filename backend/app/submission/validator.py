"""
Submission validator wrapper.

Provides a simple interface around the official Redrob
submission validator.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


class SubmissionValidator:
    """
    Wrapper around the official validation script.
    """

    def __init__(self, validator_script: str | Path):

        validator_script = Path(validator_script)

        spec = importlib.util.spec_from_file_location(
            "redrob_validator",
            validator_script,
        )

        if spec is None or spec.loader is None:
            raise ImportError(
                f"Unable to load validator from {validator_script}"
            )

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        self._validator = module.validate_submission

    def validate(
        self,
        csv_path: str | Path,
    ) -> list[str]:

        return self._validator(csv_path)

    def is_valid(
        self,
        csv_path: str | Path,
    ) -> bool:

        return len(self.validate(csv_path)) == 0