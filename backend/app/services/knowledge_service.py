import json
from pathlib import Path
from typing import Any


class KnowledgeService:
    """
    Singleton service responsible for loading
    HERMES knowledge files once.

    The knowledge is cached in memory and shared
    across all agents.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()

        return cls._instance

    def _load(self):

        knowledge_dir = (
            Path(__file__).resolve().parent.parent / "knowledge"
        )

        self.skills = self._load_json(
            knowledge_dir / "skills.json"
        )

        self.roles = self._load_json(
            knowledge_dir / "roles.json"
        )

        self.education = self._load_json(
            knowledge_dir / "education.json"
        )

        self.certifications = self._load_json(
            knowledge_dir / "certifications.json"
        )

        self.industries = self._load_json(
            knowledge_dir / "industries.json"
        )

        self.synonyms = self._load_json(
            knowledge_dir / "synonyms.json"
        )

        # -----------------------------------------
        # Fast lookup indexes
        # -----------------------------------------

        self.skill_index = {}
        self.role_index = {}
        self.certification_index = {}

        # Skills
        for category, skills in self.skills.items():
            for skill in skills:
                self.skill_index[skill.lower()] = category

        # Roles
        for category, roles in self.roles.items():
            for role in roles:
                self.role_index[role.lower()] = category

        # Certifications
        for category, certs in self.certifications.items():
            for cert in certs:
                self.certification_index[cert.lower()] = category

    @staticmethod
    def _load_json(path: Path) -> dict[str, Any]:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)