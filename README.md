# 🚀 HERMES-V1
### Hierarchical Explainable Resume Matching & Evaluation System

HERMES-V1 is an enterprise-inspired AI-powered Resume Screening and Candidate Ranking System designed for large-scale hiring. It combines traditional Information Retrieval (IR), semantic search concepts, explainable ranking, and modular AI agents to identify the most relevant candidates for a given Job Description (JD).

The project was developed as a modular offline-first architecture with scalability, explainability, and maintainability as primary goals.

---

# 🎯 Problem Statement

Recruiters often receive thousands of resumes for a single job posting.

Traditional Applicant Tracking Systems (ATS) primarily rely on keyword matching, which often:

- Misses semantically relevant candidates
- Cannot explain why candidates are ranked
- Performs poorly on synonyms and related skills
- Does not provide recruiter-friendly reasoning

HERMES-V1 addresses these limitations through a modular retrieval and ranking architecture.

---

# ✨ Key Features

- Hybrid Resume Retrieval
- BM25-based Candidate Search
- Modular AI Agent Architecture
- Explainable Candidate Ranking
- Structured Feature Engineering
- Knowledge-driven Skill Matching
- Resume Normalization Pipeline
- Configurable Ranking Engine
- Recruiter-friendly Reasoning Generation
- Offline CPU Execution
- Deterministic Ranking
- Official Hackathon CSV Export

---

# 🏗 System Architecture

```text
                    Job Description
                           │
                           ▼
                 Job Profile Builder
                           │
                           ▼
                  Candidate Loader
                           │
                           ▼
                  Document Builder
                           │
                           ▼
                  Retrieval Indexes
                  ┌──────────────┐
                  │    BM25      │
                  │ Embeddings*  │
                  └──────────────┘
                           │
                           ▼
                  Hybrid Retriever
                           │
                           ▼
                 Intelligence Layer
        ┌─────────────────────────────────┐
        │ Skill Agent                     │
        │ Career Agent                    │
        │ Project Agent                   │
        │ Company Agent                   │
        │ Behavior Agent                  │
        │ Risk Agent                      │
        └─────────────────────────────────┘
                           │
                           ▼
                  Feature Builder
                           │
                           ▼
                  Ranking Engine
                           │
                           ▼
                 Reasoning Engine
                           │
                           ▼
                Submission Generator
                           │
                           ▼
                   Official CSV Output
```

> **Note:** For the final hackathon submission, BM25 retrieval was used to meet runtime constraints on a 100K-candidate dataset. The architecture supports dense embedding retrieval and hybrid score fusion.

---

# 📂 Project Structure

```text
backend/
│
├── app/
│   ├── agents/
│   ├── bm25/
│   ├── embeddings/
│   ├── features/
│   ├── intelligence/
│   ├── knowledge/
│   ├── pipelines/
│   ├── ranking/
│   ├── reasoning/
│   ├── retrieval/
│   ├── submission/
│   └── services/
│
├── tests/
│
├── run_submission.py
└── main.py
```

---

# 🧠 Development Phases

## Phase 1 — Foundation

- Project structure
- FastAPI setup
- Candidate models
- Configuration
- Dependency management

---

## Phase 2 — Intelligence Layer

Implemented modular AI agents for structured resume understanding.

Agents include:

- Skill Agent
- Career Agent
- Project Agent
- Company Agent
- Behavior Agent
- Risk Agent

Each agent is responsible for a single intelligence task, following the Single Responsibility Principle (SRP).

---

## Phase 3 — Retrieval Layer

Implemented enterprise-style candidate retrieval.

Components:

- Resume normalization
- Retrieval document generation
- BM25 indexing
- Dense embedding indexing
- Hybrid retrieval framework

---

## Phase 4 — Feature Engineering

Converts retrieval outputs and intelligence profiles into normalized numerical features.

Feature groups include:

- Retrieval Features
- Skill Features
- Experience Features
- Project Features
- Education Features
- Behavioral Features
- Trust Features
- Risk Features

---

## Phase 5 — Ranking Layer

Computes the final candidate score.

Pipeline:

```text
Feature Vector
        │
        ▼
Feature Aggregation
        │
        ▼
Score Fusion
        │
        ▼
Risk Adjustment
        │
        ▼
Behavior Adjustment
        │
        ▼
Final Ranking Score
```

---

## Phase 6 — Explainability

Generates recruiter-friendly explanations.

Pipeline:

```text
Evidence Collection
        │
        ▼
Explanation Rules
        │
        ▼
Explanation Builder
        │
        ▼
Formatted Recruiter Reasoning
```

---

## Phase 7 — Submission Layer

Produces the official hackathon CSV.

Features:

- Deterministic ranking
- Automatic ranking assignment
- Top-100 export
- CSV validation

---

## Phase 8 — End-to-End Integration

Integrated the complete workflow into a single execution pipeline.

Workflow:

```text
Candidate Loading
        │
        ▼
Index Building
        │
        ▼
Candidate Retrieval
        │
        ▼
Feature Construction
        │
        ▼
Ranking
        │
        ▼
Reasoning
        │
        ▼
CSV Generation
```

---

# 🔍 Retrieval Strategy

HERMES-V1 was designed around a hybrid retrieval architecture.

### BM25

Advantages:

- Fast
- Excellent lexical matching
- Strong baseline retrieval

### Dense Embeddings

Advantages:

- Semantic similarity
- Synonym matching
- Context-aware search

### Hybrid Retrieval

Combines both approaches for improved recall and precision.

---

# 📊 Ranking Strategy

Candidate ranking considers multiple dimensions:

- Retrieval relevance
- Skill alignment
- Professional experience
- Project relevance
- Education
- Behavioral indicators
- Risk assessment

The architecture supports configurable weighting for each feature group.

---

# 💡 Explainable AI

Unlike traditional ATS systems, HERMES-V1 generates recruiter-friendly explanations describing why a candidate was recommended.

Example:

> Recommended due to strong alignment with Python and Machine Learning, relevant professional experience, and strong project portfolio.

---

# ⚙️ Technologies Used

- Python 3.12
- FastAPI
- BM25 (rank_bm25)
- Sentence Transformers
- NumPy
- Pydantic
- Pytest

---

# 🧪 Testing

Unit tests were implemented for multiple modules including:

- Feature Builder
- Ranking Engine
- Feature Aggregator
- Score Fusion
- Risk Adjustment
- Behavior Adjustment
- Reasoning Engine

---

# 🚀 Performance

Designed for:

- 100,000+ candidate datasets
- CPU execution
- Deterministic ranking
- Modular scalability

---

# 🔮 Future Improvements

- Full Hybrid Retrieval (BM25 + Dense Embeddings)
- Cross-Encoder Re-ranking
- Learning-to-Rank (LTR)
- Large Language Model (LLM)-based explanations
- Vector database integration
- Recruiter feedback loop
- Online learning
- GPU acceleration
- Multi-job parallel ranking
- REST API deployment

---

# 🏆 Why HERMES-V1?

✔ Modular architecture

✔ Explainable recommendations

✔ Scalable design

✔ Enterprise-inspired pipeline

✔ Offline execution

✔ Deterministic and reproducible ranking

✔ Easy to extend and maintain

---

# 📄 Hackathon Submission

The submission includes:

- Source code
- Presentation (PDF)
- Ranked candidate CSV in the official format

The system successfully generates a validated submission file compliant with the hackathon requirements.

---

# 👨‍💻 Author

**B Ankith Kumar**

Built for the Redrob AI Resume Screening Hackathon.