"""Tests for utility functions."""

import pytest
from src.utils.helpers import format_response, parse_input
from src.utils.logger import get_logger


class TestHelpers:
    """Test helper functions."""

    def test_format_response(self):
        """Test response formatting."""
        data = {"key": "value"}
        result = format_response(data)
        assert isinstance(result, str)
        assert "key" in result

    def test_parse_input(self):
        """Test input parsing."""
        text = "test input"
        result = parse_input(text)
        assert isinstance(result, dict)
        assert result["input"] == text


class TestLogger:
    """Test logger configuration."""

    def test_get_logger(self):
        """Test getting a logger."""
        logger = get_logger(__name__)
        assert logger is not None
        assert len(logger.handlers) > 0
