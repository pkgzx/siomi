import asyncio

from src.app.application.use_case.llm_use_case import LLMUseCase
from src.app.infrastructure.adapter.ai.AzureOpenAILLM import AzureOpenAILLM
from src.app.application.dto.user_message_dto import UserMessageDto

async def main():
    azure_openai_adapter = AzureOpenAILLM()
    llm_use_case = LLMUseCase(llm_service=azure_openai_adapter)
    ouput = await llm_use_case.generate_response(UserMessageDto(content="Hello"))
    print(ouput)
    


if __name__ == "__main__":
    asyncio.run(main())
