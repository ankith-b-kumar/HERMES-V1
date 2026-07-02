from __future__ import annotations

from collections.abc import Iterable

from app.models.candidate import Candidate
from app.retrieval.document_builder import DocumentBuilder
from app.retrieval.hybrid_retriever import HybridRetriever
from app.retrieval.retrieval_document import RetrievalDocument
from app.retrieval.retrieval_index import RetrievalIndex


class IndexBuilder:
    """
    Builds retrieval documents and indexes.
    """

    def __init__(
        self,
        retriever: HybridRetriever,
    ) -> None:

        self.retriever = retriever
        self.document_builder = DocumentBuilder()

    def build(
        self,
        candidates: Iterable[Candidate],
    ) -> RetrievalIndex:

        candidate_lookup: dict[str, Candidate] = {}

        document_lookup: dict[str, RetrievalDocument] = {}

        documents: list[RetrievalDocument] = []

        for candidate in candidates:

            candidate_lookup[candidate.id] = candidate

            document = self.document_builder.build(candidate)

            document_lookup[document.candidate_id] = document

            documents.append(document)

        self.retriever.build(documents)

        return RetrievalIndex(
            candidate_lookup=candidate_lookup,
            document_lookup=document_lookup,
        )