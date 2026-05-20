"""Configuration management."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    def __init__(self):
        self.env = os.getenv("ENV", "development")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.api_host = os.getenv("API_HOST", "localhost")
        self.api_port = int(os.getenv("API_PORT", 8000))
        self.api_debug = os.getenv("API_DEBUG", "false").lower() == "true"
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./soma_ai.db")
        self.ai_model = os.getenv("AI_MODEL", "gpt-3.5-turbo")
        self.ai_api_key = os.getenv("AI_API_KEY")

    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.env == "development"

    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.env == "production"
