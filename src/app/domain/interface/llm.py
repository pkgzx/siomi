from abc import ABC, abstractmethod
from src.app.domain.model.message import Message

class LLM(ABC):
    """Interface of AI LLM"""

    @abstractmethod
    async def generate(self, message: Message) -> Message:
        """Send request to llm to obtain response"""
    