from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass(slots=True)
class Candidate:
    """
    Canonical candidate model shared by every module.

    This model represents normalized candidate data after ingestion.
    It should not contain retrieval or ranking artifacts.
    """

    # -------------------------------------------------
    # Basic Information
    # -------------------------------------------------

    id: str
    name: str = ""
    email: str = ""
    phone: str = ""

    # -------------------------------------------------
    # Resume Content
    # -------------------------------------------------

    resume_text: str = ""

    # -------------------------------------------------
    # Professional Profile
    # -------------------------------------------------

    current_role: str = ""
    years_of_experience: float = 0.0
    location: str = ""

    # -------------------------------------------------
    # Structured Sections
    # -------------------------------------------------

    skills: List[str] = field(default_factory=list)

    education: List[Dict[str, Any]] = field(default_factory=list)

    experience: List[Dict[str, Any]] = field(default_factory=list)

    projects: List[Dict[str, Any]] = field(default_factory=list)

    certifications: List[Dict[str, Any]] = field(default_factory=list)

    # -------------------------------------------------
    # Additional Metadata
    # -------------------------------------------------

    metadata: Dict[str, Any] = field(default_factory=dict)