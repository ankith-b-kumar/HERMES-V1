from app.ingestion.candidate_loader import CandidateLoader


def test_load_first_candidate():

    loader = CandidateLoader()

    candidate = next(loader.load())

    assert candidate.id != ""

    assert candidate.current_role != ""

    assert len(candidate.skills) > 0

    assert candidate.resume_text != ""