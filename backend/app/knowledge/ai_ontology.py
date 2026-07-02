"""
AI Knowledge Ontology

Stores hierarchical relationships between AI concepts.

Used by:
- JD Intelligence Agent
- Skill Intelligence Agent
- Retrieval Layer
"""

from app.knowledge.base_graph import BaseGraph


class AIOntology(BaseGraph):
    """Hierarchical AI knowledge graph."""

    def _build(self) -> None:

        # Root

        self._add("Artificial Intelligence", "Machine Learning")
        self._add("Artificial Intelligence", "Deep Learning")
        self._add("Artificial Intelligence", "Natural Language Processing")
        self._add("Artificial Intelligence", "Computer Vision")
        self._add("Artificial Intelligence", "Generative AI")
        self._add("Artificial Intelligence", "Robotics")

        # Machine Learning

        self._add("Machine Learning", "Supervised Learning")
        self._add("Machine Learning", "Unsupervised Learning")
        self._add("Machine Learning", "Reinforcement Learning")

        # Deep Learning

        self._add("Deep Learning", "CNN")
        self._add("Deep Learning", "RNN")
        self._add("Deep Learning", "LSTM")
        self._add("Deep Learning", "Transformer")
        self._add("Deep Learning", "GAN")
        self._add("Deep Learning", "Autoencoder")

        # NLP

        self._add("Natural Language Processing", "BERT")
        self._add("Natural Language Processing", "GPT")
        self._add("Natural Language Processing", "T5")
        self._add("Natural Language Processing", "Sentence Transformers")
        self._add("Natural Language Processing", "Tokenization")

        # Computer Vision

        self._add("Computer Vision", "YOLO")
        self._add("Computer Vision", "OpenCV")
        self._add("Computer Vision", "Image Segmentation")
        self._add("Computer Vision", "Object Detection")

        # Generative AI

        self._add("Generative AI", "Large Language Models")
        self._add("Generative AI", "Diffusion Models")
        self._add("Generative AI", "Prompt Engineering")
        self._add("Generative AI", "Retrieval-Augmented Generation")
        self._add("Generative AI", "Agents")