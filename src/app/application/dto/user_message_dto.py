from pydantic import BaseModel, Field

class UserMessageDto(BaseModel):
    """User message from user"""
    content: str = Field(min_length=1, max_length=2000,  examples="Hello",  description="Text content of message")