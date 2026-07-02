from __future__ import annotations

from app.bm25.bm25_index import BM25Index
from app.embeddings.embedding_index import EmbeddingIndex
from app.retrieval.retrieval_document import RetrievalDocument
from app.retrieval.retrieval_result import RetrievalResult


class HybridRetriever:
    """
    BM25-first retriever.

    NOTE:
    Embedding retrieval is temporarily disabled for the
    hackathon submission to keep runtime practical on
    CPU with 100,000 candidates.
    """

    def __init__(
        self,
        bm25: BM25Index,
        embedding: EmbeddingIndex,
        bm25_weight: float = 0.5,
        embedding_weight: float = 0.5,
    ):
        self.bm25 = bm25
        self.embedding = embedding

        total = bm25_weight + embedding_weight

        if total <= 0:
            raise ValueError(
                "Retriever weights must sum to a positive value."
            )

        self.bm25_weight = bm25_weight / total
        self.embedding_weight = embedding_weight / total

    # ---------------------------------------------------------
    # Index Building
    # ---------------------------------------------------------

    def build(
        self,
        documents: list[RetrievalDocument],
    ) -> None:
        """
        Build the retrieval index.

        Only BM25 is built for the submission.
        """

        self.bm25.build(documents)

        # Disabled for submission runtime.
        # self.embedding.build(documents)

    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------

    def search(
        self,
        query: str,
        top_k: int = 100,
    ) -> list[RetrievalResult]:
        """
        Perform BM25 retrieval.

        Metadata is preserved so downstream code
        remains unchanged.
        """

        bm25_results = self.bm25.search(
            query=query,
            top_k=top_k,
        )

        final_results = []

        for result in bm25_results:

            final_results.append(
                RetrievalResult(
                    document=result.document,
                    score=result.score,
                    source="bm25",
                    metadata={
                        "bm25": result.score,
                        "embedding": 0.0,
                    },
                )
            )

        return final_results