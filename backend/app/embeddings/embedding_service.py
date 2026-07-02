from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingService:
    """
    Singleton service responsible for loading the embedding model once.

    The model is cached in memory and shared across all retrieval components.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2"
            )

        return cls._instance

    def encode(self, text: str) -> np.ndarray:
        """
        Generate a normalized embedding.
        """

        return self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )