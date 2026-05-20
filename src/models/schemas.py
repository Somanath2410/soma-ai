"""Pydantic schemas for data validation."""

from pydantic import BaseModel, Field
from typing import Optional


class PromptRequest(BaseModel):
    """Schema for prompt request."""
    
    prompt: str = Field(..., min_length=1, max_length=2000)
    model: Optional[str] = None
    temperature: Optional[float] = Field(default=0.7, ge=0.0, le=1.0)


class AIResponse(BaseModel):
    """Schema for AI response."""
    
    response: str
    model: str
    tokens_used: Optional[int] = None
    success: bool = True


class ErrorResponse(BaseModel):
    """Schema for error response."""
    
    error: str
    details: Optional[str] = None
    success: bool = False
