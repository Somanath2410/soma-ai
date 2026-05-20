"""FastAPI application setup."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.core.config import Config
from src.api.routes import health, chat
from src.utils.logger import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage app lifespan."""
    logger.info("Starting Soma AI API...")
    yield
    logger.info("Shutting down Soma AI API...")


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    config = Config()
    
    app = FastAPI(
        title="Soma AI",
        description="AI Assistant API",
        version="0.1.0",
        lifespan=lifespan,
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    app.include_router(health.router, prefix="/api/health", tags=["health"])
    app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
    
    logger.info("FastAPI application created successfully")
    return app


app = create_app()
