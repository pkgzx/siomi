from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities import Message


class IMessageRepository(ABC):
    """Interface for message persistence operations."""

    @abstractmethod
    async def save(self, message: Message) -> Message:
        """Save a message."""

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Message | None:
        """Get a message by ID."""

    @abstractmethod
    async def get_by_conversation_id(self, id: UUID, limit: int = 100) -> list[Message]:
        """Get all messages for a conversation"""