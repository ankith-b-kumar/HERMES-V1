from app.retrieval.hybrid_retriever import HybridRetriever
from app.retrieval.retrieval_document import RetrievalDocument
from app.retrieval.retrieval_result import RetrievalResult


class FakeRetriever:
    def __init__(self, results):
        self._results = results

    def search(self, query, top_k=100):
        return self._results[:top_k]


def make_document(candidate_id: str):
    return RetrievalDocument(
        candidate_id=candidate_id,
        text="dummy",
        sections={},
        token_count=1,
    )


def test_hybrid_combines_scores():

    doc1 = make_document("1")
    doc2 = make_document("2")

    bm25 = FakeRetriever([
        RetrievalResult(doc1, 10.0, "bm25"),
        RetrievalResult(doc2, 5.0, "bm25"),
    ])

    embedding = FakeRetriever([
        RetrievalResult(doc1, 0.8, "embedding"),
        RetrievalResult(doc2, 0.4, "embedding"),
    ])

    retriever = HybridRetriever(
        bm25=bm25,
        embedding=embedding,
    )

    results = retriever.search("python")

    assert len(results) == 2
    assert results[0].document.candidate_id == "1"
    assert results[0].source == "hybrid"


def test_empty_results():

    bm25 = FakeRetriever([])
    embedding = FakeRetriever([])

    retriever = HybridRetriever(
        bm25=bm25,
        embedding=embedding,
    )

    assert retriever.search("python") == []


def test_invalid_weights():

    bm25 = FakeRetriever([])
    embedding = FakeRetriever([])

    try:
        HybridRetriever(
            bm25=bm25,
            embedding=embedding,
            bm25_weight=0,
            embedding_weight=0,
        )
        assert False
    except ValueError:
        pass