from unittest.mock import patch

import pytest

# Mock API key for testing
MOCK_API_KEY = "test_api_key"


@pytest.fixture(autouse=True)
def mock_api_key():
    """Mock the API key for testing."""
    with patch("app.config.CONFIG.flowkit_python_api_key", MOCK_API_KEY):
        yield
