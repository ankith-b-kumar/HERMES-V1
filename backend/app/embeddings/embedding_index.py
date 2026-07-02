from __future__ import annotations

from typing import Optional

import numpy as np

from app.embeddings.embedding_protocol import EmbeddingEncoder
from app.retrieval.retrieval_document import RetrievalDocument
from app.retrieval.retrieval_result import RetrievalResult


class EmbeddingIndex:
    """
    Dense vector index for semantic retrieval.
    """

    def __init__(
        self,
        service: Optional[EmbeddingEncoder] = None,
    ):
        # Lazy import so unit tests don't load SentenceTransformer
        if service is None:
            from app.embeddings.embedding_service import EmbeddingService

            service = EmbeddingService()

        self.service = service
        self.documents: list[RetrievalDocument] = []
        self.embeddings: np.ndarray | None = None

    def build(
        self,
        documents: list[RetrievalDocument],
    ) -> None:
        """
        Build the embedding index from retrieval documents.
        """

        self.documents = documents

        vectors = [
            self.service.encode(doc.text)
            for doc in documents
        ]

        if vectors:
            self.embeddings = np.vstack(vectors)
        else:
            self.embeddings = np.empty((0, 384))

    def search(
        self,
        query: str,
        top_k: int = 100,
    ) -> list[RetrievalResult]:
        """
        Search using cosine similarity.
        """

        if self.embeddings is None:
            raise RuntimeError(
                "Embedding index has not been built."
            )

        if not query.strip():
            return []

        query_vector = self.service.encode(query)

        # Since embeddings are normalized,
        # dot product == cosine similarity.
        scores = self.embeddings @ query_vector

        ranked = sorted(
            zip(self.documents, scores),
            key=lambda item: item[1],
            reverse=True,
        )

        return [
            RetrievalResult(
                document=document,
                score=float(score),
                source="embedding",
            )
            for document, score in ranked[:top_k]
        ]