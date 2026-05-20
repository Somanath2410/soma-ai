"""Tests for core functionality."""

import pytest
from src.core.config import Config
from src.core.ai_engine import AIEngine


class TestConfig:
    """Test configuration class."""

    def test_config_initialization(self):
        """Test that config initializes correctly."""
        config = Config()
        assert config is not None
        assert config.env in ["development", "production"]

    def test_config_development(self):
        """Test development mode detection."""
        config = Config()
        assert isinstance(config.is_development(), bool)


class TestAIEngine:
    """Test AI Engine class."""

    def test_ai_engine_initialization(self):
        """Test that AI Engine initializes correctly."""
        config = Config()
        engine = AIEngine(config)
        assert engine is not None
        assert engine.config == config

    def test_ai_engine_process(self):
        """Test AI Engine process method."""
        config = Config()
        engine = AIEngine(config)
        result = engine.process("test prompt")
        assert isinstance(result, str)
