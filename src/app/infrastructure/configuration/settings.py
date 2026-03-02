from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings"""

    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_URL: str
    AZURE_OPENAI_API_VERSION: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
