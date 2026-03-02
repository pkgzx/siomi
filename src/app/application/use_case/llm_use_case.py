from src.app.application.mapper.message_mapper import MessageMapper
from src.app.application.dto.user_message_dto import UserMessageDto
from src.app.application.dto.response_message_dto import ResponseMessageDto
from src.app.domain.interface.llm import  LLM



class LLMUseCase:
 """LLM use cases to invoke AI Model"""

 def __init__(self, llm_service: LLM):
   self.llm = llm_service
    
 async def generate_response(self, message_dto: UserMessageDto) -> ResponseMessageDto:
    """Send message to LLM and response to user with llm generated"""
    message = MessageMapper.to_model(message_dto)
    llm_message = await self.llm.generate(message)
    return MessageMapper.to_dto(llm_message)