from dataclasses import dataclass

from app.models.candidate import Candidate
from app.retrieval.retrieval_document import RetrievalDocument


@dataclass(slots=True, frozen=True)
class RetrievalIndex:
    """
    Lookup tables produced while building retrieval indexes.

    These mappings allow downstream stages to efficiently
    recover the original Candidate and RetrievalDocument
    after hybrid retrieval.
    """

    candidate_lookup: dict[str, Candidate]

    document_lookup: dict[str, RetrievalDocument]