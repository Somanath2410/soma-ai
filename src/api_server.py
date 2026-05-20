"""Main entry point running FastAPI server."""

import uvicorn
from src.app import app
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """Run the FastAPI server."""
    logger.info("Starting Soma AI FastAPI server...")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    main()
