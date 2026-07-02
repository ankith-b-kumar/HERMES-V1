from rank_bm25 import BM25Okapi

from app.bm25.tokenizer import Tokenizer
from app.retrieval.retrieval_document import RetrievalDocument
from app.retrieval.retrieval_result import RetrievalResult


class BM25Index:
    """
    BM25 index over RetrievalDocuments.
    """

    def __init__(self):

        self.tokenizer = Tokenizer()

        self.documents: list[RetrievalDocument] = []

        self.corpus: list[list[str]] = []

        self.index: BM25Okapi | None = None

    def build(
        self,
        documents: list[RetrievalDocument],
    ) -> None:
        """
        Build the BM25 index.
        """

        self.documents = documents

        self.corpus = [
            self.tokenizer.tokenize(doc.text)
            for doc in documents
        ]

        self.index = BM25Okapi(self.corpus)

    def search(
        self,
        query: str,
        top_k: int = 100,
    ) -> list[RetrievalResult]:
        """
        Search the BM25 index.
        """

        if self.index is None:
            raise RuntimeError(
                "BM25 index has not been built."
            )

        query_tokens = self.tokenizer.tokenize(query)

        if not query_tokens:
            return []

        scores = self.index.get_scores(query_tokens)

        ranked = sorted(
            zip(self.documents, scores),
            key=lambda item: item[1],
            reverse=True,
        )

        return [
            RetrievalResult(
                document=document,
                score=float(score),
                source="bm25",
            )
            for document, score in ranked[:top_k]
        ]