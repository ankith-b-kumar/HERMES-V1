from __future__ import annotations

from app.bm25.bm25_index import BM25Index
from app.embeddings.embedding_index import EmbeddingIndex
from app.retrieval.retrieval_result import RetrievalResult


class HybridRetriever:
    """
    Combines BM25 and semantic retrieval using weighted score fusion.
    """

    def __init__(
        self,
        bm25: BM25Index,
        embedding: EmbeddingIndex,
        bm25_weight: float = 0.5,
        embedding_weight: float = 0.5,
    ):
        total = bm25_weight + embedding_weight

        if total <= 0:
            raise ValueError(
                "Retriever weights must sum to a positive value."
            )

        self.bm25 = bm25
        self.embedding = embedding

        self.bm25_weight = bm25_weight / total
        self.embedding_weight = embedding_weight / total

    def _normalize(
        self,
        results: list[RetrievalResult],
    ) -> dict[str, float]:
        """
        Min-max normalize retrieval scores.
        """

        if not results:
            return {}

        scores = [r.score for r in results]

        minimum = min(scores)
        maximum = max(scores)

        if minimum == maximum:
            return {
                r.document.candidate_id: 1.0
                for r in results
            }

        normalized = {}

        for r in results:
            normalized[r.document.candidate_id] = (
                (r.score - minimum)
                / (maximum - minimum)
            )

        return normalized

    def search(
        self,
        query: str,
        top_k: int = 100,
    ) -> list[RetrievalResult]:

        bm25_results = self.bm25.search(query, top_k)
        embedding_results = self.embedding.search(query, top_k)

        bm25_scores = self._normalize(bm25_results)
        embedding_scores = self._normalize(embedding_results)

        documents = {}

        for result in bm25_results:
            documents[result.document.candidate_id] = result.document

        for result in embedding_results:
            documents[result.document.candidate_id] = result.document

        final_results = []

        for candidate_id, document in documents.items():

            bm25_score = bm25_scores.get(candidate_id, 0.0)
            embedding_score = embedding_scores.get(candidate_id, 0.0)

            final_score = (
                self.bm25_weight * bm25_score
                + self.embedding_weight * embedding_score
            )

            final_results.append(
                RetrievalResult(
                    document=document,
                    score=final_score,
                    source="hybrid",
                    metadata={
                        "bm25": bm25_score,
                        "embedding": embedding_score,
                    },
                )
            )

        final_results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return final_results[:top_k]