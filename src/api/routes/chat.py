"""Chat/AI endpoints."""

from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel, Field

from src.core.ai_engine import AIEngine
from src.core.config import Config
from src.models.schemas import PromptRequest, AIResponse, ErrorResponse
from src.utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()


def get_ai_engine() -> AIEngine:
    """Get AI Engine instance."""
    config = Config()
    return AIEngine(config)


@router.post("/process", response_model=AIResponse)
async def process_prompt(
    request: PromptRequest,
    engine: AIEngine = Depends(get_ai_engine)
) -> AIResponse:
    """
    Process a prompt using the AI engine.
    
    Args:
        request: PromptRequest with prompt and optional parameters
        engine: AI Engine instance
        
    Returns:
        AIResponse with the AI's response
        
    Raises:
        HTTPException: If processing fails
    """
    try:
        logger.info(f"Processing prompt: {request.prompt[:50]}...")
        
        # Process the prompt
        response = engine.process(request.prompt)
        
        return AIResponse(
            response=response,
            model=engine.model,
            tokens_used=None,
            success=True
        )
    except Exception as e:
        logger.error(f"Error processing prompt: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to process prompt"
        )


@router.post("/chat")
async def chat_endpoint(
    request: PromptRequest,
    engine: AIEngine = Depends(get_ai_engine)
) -> dict:
    """
    Chat endpoint for interactive conversations.
    
    Args:
        request: PromptRequest with user message
        engine: AI Engine instance
        
    Returns:
        Dictionary with conversation data
    """
    try:
        logger.info(f"Chat message received: {request.prompt[:50]}...")
        
        response = engine.process(request.prompt)
        
        return {
            "success": True,
            "message": request.prompt,
            "response": response,
            "model": engine.model,
            "timestamp": None
        }
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Chat processing failed"
        )


@router.get("/models")
async def list_models(engine: AIEngine = Depends(get_ai_engine)):
    """
    List available AI models.
    
    Returns:
        List of available models
    """
    logger.info("Listing available models")
    
    models = [
        {
            "id": "gpt-3.5-turbo",
            "name": "GPT-3.5 Turbo",
            "provider": "OpenAI"
        },
        {
            "id": "gpt-4",
            "name": "GPT-4",
            "provider": "OpenAI"
        },
        {
            "id": "claude-3-opus",
            "name": "Claude 3 Opus",
            "provider": "Anthropic"
        }
    ]
    
    return {
        "success": True,
        "models": models,
        "current_model": engine.model
    }
