from fastapi import  Depends, APIRouter

from src.app.application.use_case.llm_use_case import LLMUseCase
from src.app.application.dto.user_message_dto import UserMessageDto
from src.app.application.dto.response_message_dto import ResponseMessageDto
from src.app.infrastructure.configuration.di_container import get_llm_use_case

chat_router = APIRouter(prefix="/chat", tags=["Chat"])

@chat_router.post("/completation")
async def generate(dto: UserMessageDto, llm_service: LLMUseCase = Depends(get_llm_use_case)) -> ResponseMessageDto:
    """Http handler to generate llm response"""
    ouput = await llm_service.generate_response(dto)
    return ouput