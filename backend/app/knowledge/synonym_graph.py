"""
Synonym Graph

Maps abbreviations, aliases, and alternate spellings
to a canonical concept while preserving display casing.
"""


class SynonymGraph:
    """Case-insensitive synonym lookup."""

    def __init__(self) -> None:
        self.graph: dict[str, str] = {}
        self._build()

    def _add(self, canonical: str, *aliases: str) -> None:
        """
        Register a canonical term and its aliases.

        All lookups are case-insensitive while the returned value
        preserves the canonical display format.
        """
        self.graph[canonical.lower()] = canonical

        for alias in aliases:
            self.graph[alias.lower()] = canonical

    def _build(self) -> None:

        # Machine Learning
        self._add(
            "Machine Learning",
            "ML",
            "Predictive Modeling",
            "Statistical Learning",
        )

        # Deep Learning
        self._add(
            "Deep Learning",
            "DL",
            "Neural Networks",
        )

        # Natural Language Processing
        self._add(
            "Natural Language Processing",
            "NLP",
            "Text Analytics",
            "Language AI",
        )

        # Computer Vision
        self._add(
            "Computer Vision",
            "CV",
            "Vision AI",
            "Image Processing",
        )

        # Large Language Model
        self._add(
            "Large Language Model",
            "LLM",
            "Large Language Models",
            "Foundation Model",
        )

        # Retrieval-Augmented Generation
        self._add(
            "Retrieval-Augmented Generation",
            "RAG",
            "Retrieval Augmented Generation",
        )

        # Generative AI
        self._add(
            "Generative AI",
            "GenAI",
            "Gen AI",
            "Generative Artificial Intelligence",
        )

        # Machine Learning Operations
        self._add(
            "MLOps",
            "Machine Learning Operations",
        )

        # Continuous Integration / Continuous Delivery
        self._add(
            "CI/CD",
            "Continuous Integration",
            "Continuous Deployment",
            "Continuous Delivery",
        )

        # Kubernetes
        self._add(
            "Kubernetes",
            "K8s",
        )

    def normalize(self, term: str) -> str:
        """Return the canonical representation of a term."""
        return self.graph.get(term.lower(), term)

    def has(self, term: str) -> bool:
        """Return True if the term exists."""
        return term.lower() in self.graph

    def size(self) -> int:
        """Return the number of registered terms."""
        return len(self.graph)