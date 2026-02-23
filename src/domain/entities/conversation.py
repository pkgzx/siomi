from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime

from src.domain.entities import Message

@dataclass
class Conversation:
    """Domain entity represents a conversaction"""

    id: UUID
    created_at: datetime
    title: str | None = None
    updated_at: datetime | None = None
    messages: list[Message] = field(default_factory=list)


    def add_message(self, message: Message) -> None:
        """Add a message to the conversation"""
        self.messages.append(message)
        self.updated_at = datetime.now()

    def get_context_window(self, max_messages: int = 10) -> list[Message]:
        """Get most recent messages for context"""
        return self.messages[-max_messages]