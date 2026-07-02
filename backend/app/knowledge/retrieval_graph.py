"""
Retrieval Graph

Connects roles to their commonly associated
skills, tools, frameworks, and technologies.

Used during candidate retrieval and semantic expansion.
"""

from collections import defaultdict


class RetrievalGraph:
    def __init__(self):
        self.graph = defaultdict(set)
        self._build()

    def _add(self, node: str, *related: str):
        self.graph[node].update(related)

    def _build(self):

        # ----------------------------------
        # Machine Learning Engineer
        # ----------------------------------

        self._add(
            "Machine Learning Engineer",
            "Python",
            "Scikit-learn",
            "TensorFlow",
            "PyTorch",
            "Pandas",
            "NumPy",
            "Docker",
            "AWS",
            "Machine Learning"
        )

        # ----------------------------------
        # NLP Engineer
        # ----------------------------------

        self._add(
            "NLP Engineer",
            "Python",
            "spaCy",
            "NLTK",
            "Hugging Face",
            "Sentence Transformers",
            "Large Language Model",
            "Prompt Engineering",
            "LangChain"
        )

        # ----------------------------------
        # Computer Vision Engineer
        # ----------------------------------

        self._add(
            "Computer Vision Engineer",
            "OpenCV",
            "YOLO",
            "Detectron2",
            "PyTorch",
            "TensorFlow",
            "CUDA"
        )

        # ----------------------------------
        # Generative AI Engineer
        # ----------------------------------

        self._add(
            "Generative AI Engineer",
            "LangChain",
            "LlamaIndex",
            "OpenAI API",
            "Ollama",
            "Large Language Model",
            "Prompt Engineering",
            "Retrieval-Augmented Generation"
        )

        # ----------------------------------
        # Backend Engineer
        # ----------------------------------

        self._add(
            "Backend Engineer",
            "FastAPI",
            "Flask",
            "Django",
            "PostgreSQL",
            "Redis",
            "Docker"
        )

        # ----------------------------------
        # MLOps Engineer
        # ----------------------------------

        self._add(
            "MLOps Engineer",
            "Docker",
            "Kubernetes",
            "MLflow",
            "Kubeflow",
            "AWS",
            "Azure",
            "CI/CD"
        )

    def related(self, node: str):
        return sorted(self.graph.get(node, []))

    def has(self, node: str):
        return node in self.graph

    def all_nodes(self):
        nodes = set(self.graph.keys())

        for related in self.graph.values():
            nodes.update(related)

        return sorted(nodes)