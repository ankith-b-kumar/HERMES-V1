from __future__ import annotations

from app.models.candidate import Candidate
from app.retrieval.retrieval_document import RetrievalDocument
from app.services.text_normalizer import TextNormalizer


class DocumentBuilder:
    """
    Converts a Candidate into a canonical searchable document.

    Every retrieval algorithm (BM25, embeddings, rule matching)
    operates on this normalized representation.
    """

    def __init__(self):
        self.normalizer = TextNormalizer()

    def build(self, candidate: Candidate) -> RetrievalDocument:

        role = []
        skills = []
        experience = []
        projects = []
        education = []
        certifications = []
        resume = []

        # -----------------------------------------
        # Role
        # -----------------------------------------

        if candidate.current_role:
            role.append(candidate.current_role)

        # -----------------------------------------
        # Skills
        # -----------------------------------------

        skills.extend(candidate.skills)

        # -----------------------------------------
        # Experience
        # -----------------------------------------

        for exp in candidate.experience:

            title = exp.get("title")
            company = exp.get("company")
            description = exp.get("description")

            if title:
                experience.append(title)

            if company:
                experience.append(company)

            if description:
                experience.append(description)

        # -----------------------------------------
        # Projects
        # -----------------------------------------

        for project in candidate.projects:

            name = project.get("name")
            description = project.get("description")

            if name:
                projects.append(name)

            if description:
                projects.append(description)

        # -----------------------------------------
        # Education
        # -----------------------------------------

        for edu in candidate.education:

            degree = edu.get("degree")

            field = edu.get("field")
            if field is None:
                field = edu.get("field_of_study")

            institution = edu.get("institution")

            if degree:
                education.append(degree)

            if field:
                education.append(field)

            if institution:
                education.append(institution)

        # -----------------------------------------
        # Certifications
        # -----------------------------------------

        for cert in candidate.certifications:

            if isinstance(cert, str):
                certifications.append(cert)
                continue

            name = cert.get("name")
            issuer = cert.get("issuer")

            if name:
                certifications.append(name)

            if issuer:
                certifications.append(issuer)

        # -----------------------------------------
        # Resume
        # -----------------------------------------

        if candidate.resume_text:
            resume.append(candidate.resume_text)

        # -----------------------------------------
        # Normalize each section
        # -----------------------------------------

        sections = {
            "role": self.normalizer.normalize("\n".join(role)),
            "skills": self.normalizer.normalize("\n".join(skills)),
            "experience": self.normalizer.normalize("\n".join(experience)),
            "projects": self.normalizer.normalize("\n".join(projects)),
            "education": self.normalizer.normalize("\n".join(education)),
            "certifications": self.normalizer.normalize(
                "\n".join(certifications)
            ),
            "resume": self.normalizer.normalize("\n".join(resume)),
        }

        # -----------------------------------------
        # Canonical searchable document
        # -----------------------------------------

        ordered_sections = [
            sections["role"],
            sections["skills"],
            sections["experience"],
            sections["projects"],
            sections["education"],
            sections["certifications"],
            sections["resume"],
        ]

        document = "\n".join(
            section
            for section in ordered_sections
            if section
        )

        return RetrievalDocument(
            candidate_id=candidate.id,
            text=document,
            sections=sections,
            token_count=len(document.split()),
        )