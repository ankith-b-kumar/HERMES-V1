import numpy as np
import pytest

from app.embeddings.embedding_index import EmbeddingIndex
from app.retrieval.retrieval_document import RetrievalDocument


class FakeEmbeddingService:
    """
    Fake embedding model used only for unit tests.
    """

    def encode(self, text: str):

        text = text.lower()

        if "python" in text:
            # Normalized vector
            return np.array([1.0, 0.0])

        if "marketing" in text:
            return np.array([0.0, 1.0])

        # 45° normalized vector
        return np.array([
            0.70710678,
            0.70710678,
        ])


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
            text="marketing sales communication",
            sections={},
            token_count=3,
        ),
    ]


def test_build_embeddings():

    index = EmbeddingIndex(
        service=FakeEmbeddingService()
    )

    docs = make_documents()

    index.build(docs)

    assert index.embeddings is not None
    assert index.embeddings.shape[0] == len(docs)


def test_search_returns_results():

    index = EmbeddingIndex(
        service=FakeEmbeddingService()
    )

    index.build(make_documents())

    results = index.search("python")

    assert len(results) == 2


def test_best_match():

    index = EmbeddingIndex(
        service=FakeEmbeddingService()
    )

    index.build(make_documents())

    results = index.search("backend python")

    assert results[0].document.candidate_id == "1"
    assert results[0].source == "embedding"


def test_top_k():

    index = EmbeddingIndex(
        service=FakeEmbeddingService()
    )

    index.build(make_documents())

    results = index.search(
        "python",
        top_k=1,
    )

    assert len(results) == 1


def test_empty_query():

    index = EmbeddingIndex(
        service=FakeEmbeddingService()
    )

    index.build(make_documents())

    results = index.search("")

    assert results == []


def test_search_before_build_raises():

    index = EmbeddingIndex(
        service=FakeEmbeddingService()
    )

    with pytest.raises(RuntimeError):
        index.search("python")