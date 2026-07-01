from enum import Enum


class AgentType(str, Enum):
    """
    Defines every supported HERMES agent.
    """

    ORCHESTRATOR = "orchestrator"

    RESUME = "resume"

    JD = "jd"

    RETRIEVAL = "retrieval"

    RANKING = "ranking"

    EXPLANATION = "explanation"