"""
Skill Knowledge Graph

Represents relationships between technologies, tools,
frameworks, and broader technical domains.
"""

from app.knowledge.base_graph import BaseGraph


class SkillGraph(BaseGraph):

    def _build(self):

        # ---------------------------
        # Programming Languages
        # ---------------------------

        self._add("Programming Languages", "Python")
        self._add("Programming Languages", "Java")
        self._add("Programming Languages", "C++")
        self._add("Programming Languages", "JavaScript")
        self._add("Programming Languages", "TypeScript")
        self._add("Programming Languages", "Go")
        self._add("Programming Languages", "Rust")

        # ---------------------------
        # Python Ecosystem
        # ---------------------------

        self._add("Python", "NumPy")
        self._add("Python", "Pandas")
        self._add("Python", "Scikit-learn")
        self._add("Python", "TensorFlow")
        self._add("Python", "PyTorch")
        self._add("Python", "FastAPI")
        self._add("Python", "Flask")
        self._add("Python", "Django")

        # ---------------------------
        # Machine Learning
        # ---------------------------

        self._add("Machine Learning", "Scikit-learn")
        self._add("Machine Learning", "XGBoost")
        self._add("Machine Learning", "LightGBM")

        # ---------------------------
        # Deep Learning
        # ---------------------------

        self._add("Deep Learning", "TensorFlow")
        self._add("Deep Learning", "PyTorch")
        self._add("Deep Learning", "Keras")

        # ---------------------------
        # NLP
        # ---------------------------

        self._add("Natural Language Processing", "spaCy")
        self._add("Natural Language Processing", "NLTK")
        self._add("Natural Language Processing", "Hugging Face")
        self._add("Natural Language Processing", "Sentence Transformers")

        # ---------------------------
        # Computer Vision
        # ---------------------------

        self._add("Computer Vision", "OpenCV")
        self._add("Computer Vision", "YOLO")
        self._add("Computer Vision", "Detectron2")

        # ---------------------------
        # Generative AI
        # ---------------------------

        self._add("Generative AI", "LangChain")
        self._add("Generative AI", "LlamaIndex")
        self._add("Generative AI", "OpenAI API")
        self._add("Generative AI", "Ollama")

        # ---------------------------
        # Cloud
        # ---------------------------

        self._add("Cloud", "AWS")
        self._add("Cloud", "Azure")
        self._add("Cloud", "Google Cloud")

        self._add("AWS", "EC2")
        self._add("AWS", "S3")
        self._add("AWS", "Lambda")
        self._add("AWS", "SageMaker")

        # ---------------------------
        # DevOps
        # ---------------------------

        self._add("DevOps", "Docker")
        self._add("DevOps", "Kubernetes")
        self._add("DevOps", "GitHub Actions")
        self._add("DevOps", "Jenkins")

        # ---------------------------
        # Databases
        # ---------------------------

        self._add("Databases", "PostgreSQL")
        self._add("Databases", "MySQL")
        self._add("Databases", "MongoDB")
        self._add("Databases", "Redis")
        self._add("Databases", "SQLite")