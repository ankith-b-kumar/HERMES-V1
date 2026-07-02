"""
Role Ontology

Represents hierarchical relationships between AI and software roles.
"""

from app.knowledge.base_graph import BaseGraph


class RoleOntology(BaseGraph):

    def _build(self):

        # Root
        self._add("Artificial Intelligence Engineer", "Machine Learning Engineer")
        self._add("Artificial Intelligence Engineer", "Deep Learning Engineer")
        self._add("Artificial Intelligence Engineer", "NLP Engineer")
        self._add("Artificial Intelligence Engineer", "Computer Vision Engineer")
        self._add("Artificial Intelligence Engineer", "Generative AI Engineer")
        self._add("Artificial Intelligence Engineer", "MLOps Engineer")

        # Data Science
        self._add("Data Scientist", "Machine Learning Engineer")
        self._add("Data Scientist", "Research Scientist")

        # Software
        self._add("Software Engineer", "Backend Engineer")
        self._add("Software Engineer", "Frontend Engineer")
        self._add("Software Engineer", "Full Stack Engineer")

        # Backend
        self._add("Backend Engineer", "API Engineer")
        self._add("Backend Engineer", "Platform Engineer")

        # DevOps
        self._add("DevOps Engineer", "Cloud Engineer")
        self._add("DevOps Engineer", "Site Reliability Engineer")