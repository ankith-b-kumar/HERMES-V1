from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    """
    Central configuration for HERMES.
    No hardcoded values should exist elsewhere.
    """

    # Data
    DATASET_PATH: Path = PROJECT_ROOT / "data" / "candidates.jsonl"

    # Retrieval
    TOP_K: int = 100

    # Embeddings
    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    # Storage
    VECTOR_DB_PATH: Path = PROJECT_ROOT / "vector_db"

    # Logging
    LOG_LEVEL: str = "INFO"

    # Future LLM
    MODEL_NAME: str = "local"
    OLLAMA_ENDPOINT: str = "http://localhost:11434"


settings = Settings()