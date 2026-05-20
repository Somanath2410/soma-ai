"""Health check routes."""

from fastapi import APIRouter, HTTPException
from src.utils.logger import get_logger
from pydantic import BaseModel
from datetime import datetime

logger = get_logger(__name__)

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    timestamp: str
    version: str


@router.get("/", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        HealthResponse with status and timestamp
    """
    logger.info("Health check requested")
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="0.1.0"
    )


@router.get("/ready", response_model=HealthResponse)
async def readiness_check():
    """
    Readiness check endpoint.
    
    Returns:
        HealthResponse indicating if service is ready
    """
    logger.info("Readiness check requested")
    return HealthResponse(
        status="ready",
        timestamp=datetime.now().isoformat(),
        version="0.1.0"
    )


@router.get("/live", response_model=HealthResponse)
async def liveness_check():
    """
    Liveness check endpoint.
    
    Returns:
        HealthResponse indicating if service is alive
    """
    logger.info("Liveness check requested")
    return HealthResponse(
        status="alive",
        timestamp=datetime.now().isoformat(),
        version="0.1.0"
    )
