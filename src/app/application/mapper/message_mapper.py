from src.app.application.dto.user_message_dto import UserMessageDto
from src.app.application.dto.response_message_dto import ResponseMessageDto
from src.app.domain.model.message import Message

class MessageMapper:
    """Message class mapper to converts between dto and model objects"""

    @staticmethod
    def to_model(message_dto: UserMessageDto) -> Message:
        """Convert dto input to model"""
        return Message(content=message_dto.content)
    
    @staticmethod
    def to_dto(message: Message) -> ResponseMessageDto:
        """Convert model to dto"""
        return ResponseMessageDto(content=message.content) 