from dataclasses import dataclass

from src.app.domain.exception.business_exception import BusinessException
from src.app.domain.enum.technical_message import TechnicalMessage

@dataclass
class Message:
    """Message with content text from user"""
    content: str

    def __post_init__(self) -> None:
        if not self.content:
            raise BusinessException(TechnicalMessage.INVALID_MESSAGE_CONTENT)