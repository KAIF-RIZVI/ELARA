from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from urllib.parse import quote_plus
from pathlib import Path

env_path = Path(__file__).parent.parent.parent / ".env"

class Settings(BaseSettings):
    PROJECT_NAME: str = "ELARA Enterprise SaaS"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    
    # Security
    JWT_SECRET_KEY: str = "change_me_in_production"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Postgres Database
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "YOUR_PASSWORD"
    POSTGRES_DB: str = "elara"
    POSTGRES_PORT: int = 5432
    
    # Database URL
    DATABASE_URL: str | None = None
    
    # Redis & Celery
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Qdrant
    QDRANT_URL: str = "http://localhost:6333"
    
    # External Integrations (Optional)
    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    GOOGLE_REDIRECT_URI: str = "http://localhost:8000/api/v1/auth/google/callback"
    GITHUB_CLIENT_ID: str | None = None
    GITHUB_CLIENT_SECRET: str | None = None
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    AWS_REGION: str = "ap-south-1"
    S3_BUCKET_NAME: str | None = None
    
    # Email & SMTP
    SMTP_HOST: str | None = None
    SMTP_PORT: int = 587
    SMTP_USERNAME: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAIL_FROM: str = "noreply@elara.ai"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        encoded_password = quote_plus(self.POSTGRES_PASSWORD) if self.POSTGRES_PASSWORD else ""
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{encoded_password}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=str(env_path), 
        env_file_encoding="utf-8", 
        case_sensitive=True,
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()
