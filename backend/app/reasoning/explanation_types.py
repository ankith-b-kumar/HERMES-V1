from enum import StrEnum


class ExplanationType(StrEnum):
    """
    Types of recruiter-facing explanation messages.
    """

    HIGHLIGHT = "highlight"
    CONCERN = "concern"