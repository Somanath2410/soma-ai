"""Main entry point for Soma AI."""

import sys
from pathlib import Path

from src.core.config import Config
from src.core.ai_engine import AIEngine
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """Main function."""
    logger.info("Starting Soma AI...")
    
    config = Config()
    logger.info(f"Running in {config.env} environment")
    
    ai_engine = AIEngine(config)
    logger.info("AI Engine initialized")
    
    # Your main logic here
    logger.info("Soma AI ready!")


if __name__ == "__main__":
    main()
