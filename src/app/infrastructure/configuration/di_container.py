from src.app.infrastructure.adapter.ai.AzureOpenAILLM import AzureOpenAILLM
from src.app.application.dto.user_message_dto import UserMessageDto
from src.app.application.use_case.llm_use_case import LLMUseCase


azure_openai_adapter = AzureOpenAILLM()


def get_llm_use_case():
    "Generate singleto llm useCase to inject"
    return LLMUseCase(llm_service=azure_openai_adapter)