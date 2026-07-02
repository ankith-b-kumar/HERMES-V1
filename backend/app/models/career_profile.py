from dataclasses import dataclass, field
from typing import List


@dataclass
class CareerProfile:
    """
    Structured career evidence extracted from a resume.
    """

    total_experience_years: float = 0.0

    current_role: str = ""

    companies: List[str] = field(default_factory=list)

    job_titles: List[str] = field(default_factory=list)

    number_of_companies: int = 0

    number_of_roles: int = 0