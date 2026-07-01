from abc import ABC, abstractmethod
from typing import Any

from app.core.logger import get_logger


class BaseAgent(ABC):
    """
    Base class for all HERMES agents.

    Every agent must inherit from this class.
    """

    def __init__(self, name: str):
        self.name = name
        self.logger = get_logger(name)

    @abstractmethod
    def run(self, input_data: Any) -> Any:
        """
        Execute the agent.

        Every child agent must implement this method.
        """
        pass