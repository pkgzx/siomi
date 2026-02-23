from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass
class Message:
    """Domain entity represents a message in a conversation"""

    id: UUID
    conversation_id: UUID
    content: str
    created_at: datetime
