from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Application settings
    app_name: str = os.getenv("APP_NAME", "LLM Knowledge Extractor")
    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    
    # Server settings
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", 8000))
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # API settings
    api_prefix: str = os.getenv("API_PREFIX", "/api/v1")
    
    # Security
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()
