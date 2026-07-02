from __future__ import annotations

from typing import Any

from app.models.candidate import Candidate


class CandidateMapper:
    """
    Maps a raw dataset record into the internal Candidate model.
    """

    def map(self, record: dict[str, Any]) -> Candidate:

        profile = record.get("profile", {})

        experience = record.get("career_history", [])

        education = record.get("education", [])

        certifications = record.get("certifications", [])

        skills = [
            skill.get("name", "")
            for skill in record.get("skills", [])
            if skill.get("name")
        ]

        # -------------------------------------
        # Build searchable resume text
        # -------------------------------------

        resume_parts = []

        if profile.get("headline"):
            resume_parts.append(profile["headline"])

        if profile.get("summary"):
            resume_parts.append(profile["summary"])

        for job in experience:

            if job.get("title"):
                resume_parts.append(job["title"])

            if job.get("company"):
                resume_parts.append(job["company"])

            if job.get("description"):
                resume_parts.append(job["description"])

        resume_text = "\n".join(resume_parts)

        return Candidate(
            id=record.get("candidate_id", ""),
            name=profile.get("anonymized_name", ""),
            resume_text=resume_text,
            current_role=profile.get("current_title", ""),
            years_of_experience=float(
                profile.get("years_of_experience", 0)
            ),
            location=profile.get("location", ""),
            skills=skills,
            education=education,
            experience=experience,
            certifications=certifications,
            metadata={
                "languages": record.get("languages", []),
                "redrob_signals": record.get(
                    "redrob_signals",
                    {},
                ),
                "profile": profile,
            },
        )