from typing import Protocol
import numpy as np


class EmbeddingEncoder(Protocol):
    def encode(self, text: str) -> np.ndarray:
        ...