import pytest
from fastapi.testclient import TestClient
from app.app import app

# Initialize the test client
client = TestClient(app)

@pytest.mark.asyncio
async def test_list_functions():
    """Test listing available functions."""
    # Test splitter results
    response = client.get("/", headers={"api-key": "test_api_key"})
    assert response.status_code == 200
    response_data = response.json()
    
    expected_response_start = [
        {
            "name": "split_ppt",
            "path": "/splitter/ppt",
            "inputs": [
                {"name": "document_content", "type": "string(binary)"},
                {"name": "chunk_size", "type": "integer"},
                {"name": "chunk_overlap", "type": "integer"}
            ],
            "outputs": [
                {"name": "chunks", "type": "array<string>"}
            ],
            "definitions": {}
        },
        {
            "name": "split_py",
            "path": "/splitter/py",
            "inputs": [
                {"name": "document_content", "type": "string(binary)"},
                {"name": "chunk_size", "type": "integer"},
                {"name": "chunk_overlap", "type": "integer"}
            ],
            "outputs": [
                {"name": "chunks", "type": "array<string>"}
            ],
            "definitions": {}
        },
        {
            "name": "split_pdf",
            "path": "/splitter/pdf",
            "inputs": [
                {"name": "document_content", "type": "string(binary)"},
                {"name": "chunk_size", "type": "integer"},
                {"name": "chunk_overlap", "type": "integer"}
            ],
            "outputs": [
                {"name": "chunks", "type": "array<string>"}
            ],
            "definitions": {}
        }
    ]

    assert response_data[:3] == expected_response_start

    # Test invalid API key
    response = client.get("/", headers={"api-key": "invalid_api_key"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API key"}

