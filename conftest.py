import pytest
from pathlib import Path

@pytest.fixture
def test_dir():
    """Return the test directory path."""
    return Path(__file__).parent / "tests"

@pytest.fixture
def project_root():
    """Return the project root directory."""
    return Path(__file__).parent
