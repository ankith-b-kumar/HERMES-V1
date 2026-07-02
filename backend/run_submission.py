from pathlib import Path

from app.bm25.bm25_index import BM25Index
from app.embeddings.embedding_index import EmbeddingIndex
from app.ingestion.candidate_loader import CandidateLoader
from app.models.job_profile import JobProfile
from app.retrieval.hybrid_retriever import HybridRetriever
from app.retrieval.index_builder import IndexBuilder
from app.submission.csv_writer import CSVWriter
from app.submission.submission_models import SubmissionRow
from app.submission.validator import SubmissionValidator


def build_query(job_profile: JobProfile) -> str:
    """
    Build a retrieval query from the structured JobProfile.
    """

    parts = []

    parts.extend(job_profile.role_titles)
    parts.extend(job_profile.required_skills)
    parts.extend(job_profile.preferred_skills)
    parts.extend(job_profile.tools)
    parts.extend(job_profile.keywords)

    return " ".join(parts)


def build_reasoning(document, job_profile) -> str:
    """
    Generate concise recruiter-friendly reasoning.
    """

    sections = document.sections
    strengths = []

    skills_text = sections.get("skills", "").lower()

    matched = [
        skill
        for skill in job_profile.required_skills
        if skill.lower() in skills_text
    ]

    if matched:
        strengths.append(
            f"matches key skills ({', '.join(matched[:2])})"
        )

    if sections.get("experience", "").strip():
        strengths.append("relevant experience")

    if sections.get("projects", "").strip():
        strengths.append("relevant projects")

    if sections.get("education", "").strip():
        strengths.append("suitable education")

    if sections.get("certifications", "").strip():
        strengths.append("professional certifications")

    if not strengths:
        return "Overall profile aligns well with the job requirements."

    strengths = strengths[:3]

    if len(strengths) == 1:
        return f"Recommended due to {strengths[0]}."

    return (
        "Recommended due to "
        + ", ".join(strengths[:-1])
        + " and "
        + strengths[-1]
        + "."
    )


def main():

    print("Loading candidates...")

    loader = CandidateLoader()

    candidates = list(loader.load())

    print(f"Loaded {len(candidates)} candidates.")

    retriever = HybridRetriever(
        BM25Index(),
        EmbeddingIndex(),
    )

    print("Building retrieval indexes...")

    index_builder = IndexBuilder(retriever)

    index_builder.build(candidates)

    print("Preparing Job Profile...")

    job_profile = JobProfile(

        role_titles=[
            "Senior AI Engineer",
            "AI Engineer",
            "Machine Learning Engineer",
        ],

        required_skills=[
            "python",
            "machine learning",
            "embeddings",
            "retrieval",
            "ranking",
            "llm",
            "hybrid retrieval",
            "vector database",
            "bm25",
            "evaluation",
        ],

        preferred_skills=[
            "fine tuning",
            "lora",
            "qlora",
            "peft",
            "learning to rank",
            "xgboost",
            "distributed systems",
            "open source",
            "hr tech",
        ],

        tools=[
            "sentence transformers",
            "openai embeddings",
            "bge",
            "e5",
            "pinecone",
            "weaviate",
            "qdrant",
            "milvus",
            "opensearch",
            "elasticsearch",
            "faiss",
        ],

        education=[],

        certifications=[],

        industries=[
            "artificial intelligence",
            "machine learning",
            "recruitment",
            "talent intelligence",
            "hr tech",
        ],

        keywords=[
            "recommendation systems",
            "search",
            "semantic search",
            "ranking",
            "retrieval",
            "nlp",
            "offline evaluation",
            "ndcg",
            "mrr",
            "map",
            "a/b testing",
            "production ml",
        ],

        minimum_experience_years=5,
    )

    query = build_query(job_profile)

    print("Running hybrid retrieval...")

    results = retriever.search(
        query=query,
        top_k=100,
    )

    rows = []

    for result in results:

        rows.append(
            SubmissionRow(
                candidate_id=result.document.candidate_id,
                score=result.score,
                reasoning=build_reasoning(
                    result.document,
                    job_profile,
                ),
            )
        )

    print("Writing submission CSV...")

    writer = CSVWriter()

    output = writer.write(
        rows,
        "team_Stakers.csv",
    )

    print("Validating submission...")

    validator = SubmissionValidator(
        Path("validate_submission.py")
    )

    errors = validator.validate(output)

    if errors:

        print("\nVALIDATION FAILED\n")

        for error in errors:
            print(error)

    else:

        print("\nSubmission generated successfully!")

        print(f"Output: {output}")


if __name__ == "__main__":
    main()