from typing import Dict
from typing import List

from app.agents.agent_types import AgentType
from app.agents.base_agent import BaseAgent


class AgentRegistry:
    """
    Stores and manages all HERMES agents.

    The registry allows the Orchestrator to retrieve
    agents without knowing how they are implemented.
    """

    def __init__(self):
        self._agents: Dict[AgentType, BaseAgent] = {}

    def register(self, name: AgentType, agent: BaseAgent) -> None:
        """
        Register a new agent.

        Raises:
            ValueError: if the agent name already exists.
        """
        if name in self._agents:
            raise ValueError(f"Agent '{name}' is already registered.")

        self._agents[name] = agent

    def get(self, name: AgentType) -> BaseAgent:
        """
        Retrieve an agent by name.

        Raises:
            KeyError: if the agent is not registered.
        """
        if name not in self._agents:
            raise KeyError(f"Agent '{name}' is not registered.")

        return self._agents[name]

    def exists(self, name: AgentType) -> bool:
        """
        Check whether an agent exists.
        """
        return name in self._agents

    def list_agents(self) -> list[AgentType]:
        """
        Return all registered agent names.
        """
        return sorted(self._agents.keys(), key=lambda agent: agent.value)