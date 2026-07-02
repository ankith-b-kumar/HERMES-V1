from app.ingestion.candidate_loader import CandidateLoader
from app.retrieval.document_builder import DocumentBuilder


def test_dataset_pipeline():

    loader = CandidateLoader()

    builder = DocumentBuilder()

    candidate = next(loader.load())

    document = builder.build(candidate)

    assert document.candidate_id == candidate.id

    assert document.token_count > 0

    assert document.text