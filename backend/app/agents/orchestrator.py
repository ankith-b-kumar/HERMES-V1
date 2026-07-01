from typing import Any, Dict

from app.agents.base_agent import BaseAgent


class Orchestrator(BaseAgent):
    """
    Coordinates all HERMES agents.

    The orchestrator contains NO business logic.
    It only controls workflow.
    """

    def __init__(self):
        super().__init__("Orchestrator")

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info("Starting HERMES workflow")

        # Future workflow:
        #
        # 1. JD Agent
        # 2. Resume Agent
        # 3. Retrieval Agent
        # 4. Ranking Agent
        # 5. Explainability Agent

        self.logger.info("Workflow completed")

        return {
            "status": "success",
            "message": "Pipeline skeleton executed."
        }