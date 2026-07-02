from dataclasses import dataclass
from typing import Any

from app.retrieval.retrieval_document import RetrievalDocument


@dataclass(slots=True)
class RetrievalResult:
    """
    Canonical retrieval result shared across all retrieval algorithms.
    """

    document: RetrievalDocument

    score: float

    source: str

    metadata: dict[str, Any] | None = None