from uuid import UUID, uuid4
from datetime import datetime

from src.domain.entities.conversation import Conversation
from src.domain.entities.message import Message

class ConversationService:
    """Domain service for a conversation-related business logic."""

    def create_conversation(self, title: str | None = None) -> Conversation:
        """Create a new conversation."""
        return Conversation(
            id=uuid4(),
            title=title,
            created_at=datetime.now()
        )
    
    def create_user_message(self, conversation: Conversation, content: str) -> Message:
        """Create a user message and add it to the conversation."""
        message = Message(
            id=uuid4(),
            conversation_id=conversation.id,
            content=content,
            created_at=datetime.now()
        )

        conversation.add_message(message)

        return message
    
    