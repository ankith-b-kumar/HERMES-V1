"""
End-to-end HERMES-V1 ranking pipeline.

This pipeline coordinates the complete workflow:

Candidate Loading
    ↓
Hybrid Retrieval
    ↓
Feature Building
    ↓
Ranking
    ↓
Reasoning
    ↓
Submission Mapping
    ↓
CSV Writing
    ↓
Validation

The pipeline intentionally contains no business logic.
Each stage delegates work to its respective module.
"""

from __future__ import annotations

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class IntegrationPipeline:
    """
    Coordinates the complete HERMES-V1 ranking workflow.
    """

    def __init__(
        self,
        candidate_loader,
        retrieval_engine,
        feature_builder,
        ranking_engine,
        reasoning_engine,
        submission_mapper,
        csv_writer,
        validator,
        profiler,
    ) -> None:
        self.candidate_loader = candidate_loader
        self.retrieval_engine = retrieval_engine
        self.feature_builder = feature_builder
        self.ranking_engine = ranking_engine
        self.reasoning_engine = reasoning_engine
        self.submission_mapper = submission_mapper
        self.csv_writer = csv_writer
        self.validator = validator
        self.profiler = profiler

    def run(
        self,
        job_description,
        output_csv: str | Path,
    ) -> Path:
        """
        Execute the complete HERMES-V1 pipeline.

        Parameters
        ----------
        job_description
            Parsed job description.

        output_csv
            Destination CSV path.

        Returns
        -------
        Path
            Path to the validated submission CSV.
        """

        logger.info("Starting HERMES-V1 pipeline.")

        with self.profiler.measure("candidate_loading"):
            logger.info("Loading candidates...")
            candidates = self.candidate_loader.load()

        with self.profiler.measure("retrieval"):
            logger.info("Running hybrid retrieval...")
            retrieved_candidates = self.retrieval_engine.retrieve(
                job_description,
                candidates,
            )

        with self.profiler.measure("feature_building"):
            logger.info("Building feature vectors...")
            feature_vectors = self.feature_builder.build(
                retrieved_candidates,
                job_description,
            )

        with self.profiler.measure("ranking"):
            logger.info("Ranking candidates...")
            ranking_results = self.ranking_engine.rank(
                feature_vectors,
                job_description,
            )

        with self.profiler.measure("reasoning"):
            logger.info("Generating reasoning...")
            final_results = self.reasoning_engine.generate(
                ranking_results,
                job_description,
            )

        with self.profiler.measure("submission_mapping"):
            logger.info("Preparing submission rows...")
            submission_rows = self.submission_mapper.map(
                final_results,
            )

        with self.profiler.measure("csv_generation"):
            logger.info("Writing submission CSV...")
            csv_path = self.csv_writer.write(
                submission_rows,
                output_csv,
            )

        with self.profiler.measure("validation"):
            logger.info("Validating submission...")

            errors = self.validator.validate(csv_path)

            if errors:
                logger.error("Submission validation failed.")

                for error in errors:
                    logger.error(error)

                raise RuntimeError(
                    "Submission validation failed:\n"
                    + "\n".join(errors)
                )

        logger.info("Submission validation passed.")

        logger.info("Pipeline completed successfully.")

        logger.info("Runtime summary:")

        for stage, elapsed in self.profiler.measurements.items():
            logger.info(
                "  %-25s %.3f sec",
                stage,
                elapsed,
            )

        logger.info(
            "Total runtime: %.3f sec",
            self.profiler.total,
        )

        return csv_path