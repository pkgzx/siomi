from enum import Enum


class TechnicalMessage(Enum):
    """This is a message from app to user"""

    INTERNAL_ERROR = (500, "Something went wrong, please try again", "")
    INVALID_MESSAGE_CONTENT = (400, "The content of message must be valid", "content")

    def __init__(self, code: int, message: str, param: str):
        self.code = code
        self.message = message
        self.param = param
    
    def get_param(self) -> str:
        return self.param