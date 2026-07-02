import pytest

from app.bm25.bm25_index import BM25Index
from app.retrieval.retrieval_document import RetrievalDocument


def make_documents():
    return [
        RetrievalDocument(
            candidate_id="1",
            text="python fastapi postgres",
            sections={},
            token_count=3,
        ),
        RetrievalDocument(
            candidate_id="2",
            text="marketing sales",
            sections={},
            token_count=2,
        ),
    ]


def test_build_index():
    index = BM25Index()
    index.build(make_documents())

    assert index.index is not None


def test_search_returns_results():
    index = BM25Index()
    index.build(make_documents())

    results = index.search("python")

    assert len(results) == 2


def test_best_match_ranked_first():
    index = BM25Index()
    index.build(make_documents())

    results = index.search("python")

    assert results[0].document.candidate_id == "1"
    assert results[0].source == "bm25"


def test_top_k():
    index = BM25Index()
    index.build(make_documents())

    results = index.search("python", top_k=1)

    assert len(results) == 1


def test_empty_query():
    index = BM25Index()
    index.build(make_documents())

    results = index.search("")

    assert results == []
    
    
def test_search_before_build_raises():
    index = BM25Index()

    with pytest.raises(RuntimeError):
        index.search("python")