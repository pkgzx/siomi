from src.app.domain.interface.llm import LLM
from src.app.domain.model.message import Message
from src.app.infrastructure.configuration.settings import settings

from langchain_openai import AzureChatOpenAI

class AzureOpenAILLM(LLM):
    """Azure OpenAI implementation of LLM"""

    def __init__(self) -> None:
        self._client = AzureChatOpenAI(api_key=settings.AZURE_OPENAI_API_KEY, base_url=settings.AZURE_OPENAI_URL, api_version=settings.AZURE_OPENAI_API_VERSION)
    
    async def generate(self, message) -> Message:
        response = self._client.invoke(message.content)
        print(f"response: {response}")
        return Message(response.content)
