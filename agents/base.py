from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent's logic.
        :param context: Shared context including user state and other agent outputs.
        :return: Result of the agent's execution.
        """
        pass

    def log(self, message: str):
        print(f"[{self.name}] {message}")
