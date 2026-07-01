from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Candidate:
    """
    Canonical candidate model shared by every module.

    Every agent, service, and pipeline must consume and produce this structure.
    """

    # Basic Information
    id: str
    name: str = ""
    email: str = ""
    phone: str = ""

    # Resume Content
    resume_text: str = ""

    # Professional Profile
    current_role: str = ""
    years_of_experience: float = 0.0
    location: str = ""

    # Structured Sections
    skills: List[str] = field(default_factory=list)
    education: List[Dict[str, Any]] = field(default_factory=list)
    experience: List[Dict[str, Any]] = field(default_factory=list)
    projects: List[Dict[str, Any]] = field(default_factory=list)
    certifications: List[Dict[str, Any]] = field(default_factory=list)

    # AI Features (filled later)
    embedding: Optional[List[float]] = None

    # Additional metadata
    metadata: Dict[str, Any] = field(default_factory=dict)