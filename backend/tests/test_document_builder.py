from app.ingestion.candidate_loader import CandidateLoader
from app.retrieval.document_builder import DocumentBuilder
from app.services.text_normalizer import TextNormalizer


def get_candidate():
    return next(CandidateLoader().load())


def test_document_is_lowercase():

    candidate = get_candidate()

    builder = DocumentBuilder()

    document = builder.build(candidate)

    assert document.text == document.text.lower()


def test_document_has_role():

    candidate = get_candidate()

    builder = DocumentBuilder()

    document = builder.build(candidate)

    assert candidate.current_role.lower() in document.text


def test_document_has_skills():

    candidate = get_candidate()

    builder = DocumentBuilder()

    normalizer = TextNormalizer()

    document = builder.build(candidate)

    for skill in candidate.skills:

        normalized_skill = normalizer.normalize(skill)

        assert normalized_skill in document.text


def test_token_count():

    candidate = get_candidate()

    builder = DocumentBuilder()

    document = builder.build(candidate)

    assert document.token_count > 0