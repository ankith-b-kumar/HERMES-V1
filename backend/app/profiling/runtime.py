from __future__ import annotations

from contextlib import contextmanager
from time import perf_counter


class RuntimeProfiler:

    def __init__(self):
        self.measurements = {}

    @contextmanager
    def measure(self, stage: str):

        start = perf_counter()

        try:
            yield
        finally:
            self.measurements[stage] = (
                perf_counter() - start
            )

    @property
    def total(self):

        return sum(self.measurements.values())