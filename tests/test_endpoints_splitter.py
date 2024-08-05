import base64
from fastapi import HTTPException
import pytest
from fastapi.testclient import TestClient
from app.app import app
from app.endpoints.splitter import validate_request
from app.models.splitter import SplitterRequest
from tests.conftest import MOCK_API_KEY

# Create a test client
client = TestClient(app)

def encode_file_to_base64(file_path):
    """Encode a file to base64 string."""
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')

@pytest.mark.asyncio
async def test_split_ppt():
    """Test splitting text in a PowerPoint document into chunks."""
    ppt_content_base64 = encode_file_to_base64("./tests/test_files/test_presentation.pptx")
    request_payload = {
        "document_content": ppt_content_base64,
        "chunk_size": 100,
        "chunk_overlap": 10
    }
    response = client.post(
        "/splitter/ppt",
        json=request_payload,
        headers={"api-key": MOCK_API_KEY}
    )
    if response.status_code != 200:
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.json()}")
    assert response.status_code == 200
    assert "chunks" in response.json()

@pytest.mark.asyncio
async def test_split_py():
    """Test splitting Python code into chunks."""
    python_code = """
    def hello_world():
        print("Hello, world!")
    """
    python_code_base64 = base64.b64encode(python_code.encode()).decode('utf-8')
    request_payload = {
        "document_content": python_code_base64,
        "chunk_size": 50,
        "chunk_overlap": 5
    }
    response = client.post(
        "/splitter/py",
        json=request_payload,
        headers={"api-key": MOCK_API_KEY}
    )
    assert response.status_code == 200
    assert "chunks" in response.json()

@pytest.mark.asyncio
async def test_split_pdf():
    """Test splitting text in a PDF document into chunks."""
    pdf_content_base64 = encode_file_to_base64("./tests/test_files/test_document.pdf")
    request_payload = {
        "document_content": pdf_content_base64,
        "chunk_size": 200,
        "chunk_overlap": 20
    }
    response = client.post(
        "/splitter/pdf",
        json=request_payload,
        headers={"api-key": MOCK_API_KEY}
    )
    assert response.status_code == 200
    assert "chunks" in response.json()

# Define test cases for validate_request()
validate_request_test_cases = [
    # Test case 1: valid request
    (
        SplitterRequest(
            document_content="dGVzdA==",  # base64 for "test"
            chunk_size=100,
            chunk_overlap=10
        ),
        MOCK_API_KEY,
        None,
    ),
    # Test case: invalid API key
    (
        SplitterRequest(
            document_content="dGVzdA==",
            chunk_size=100,
            chunk_overlap=10
        ),
        "invalid_api_key",
        HTTPException(status_code=401, detail="Invalid API key"),
    ),
    # Test case 2: missing document content
    (
        SplitterRequest(
            document_content="",
            chunk_size=100,
            chunk_overlap=10
        ),
        MOCK_API_KEY,
        HTTPException(status_code=400, detail="No document content provided"),
    ),
    # Test case 4: invalid chunk size
    (
        SplitterRequest(
            document_content="dGVzdA==",
            chunk_size=0,
            chunk_overlap=10
        ),
        MOCK_API_KEY,
        HTTPException(status_code=400, detail="No chunk size provided"),
    ),
    # Test case 5: invalid chunk overlap
    (
        SplitterRequest(
            document_content="dGVzdA==",
            chunk_size=100,
            chunk_overlap=-1
        ),
        MOCK_API_KEY,
        HTTPException(status_code=400, detail="Chunk overlap must be greater than or equal to 0"),
    ),
]

@pytest.mark.parametrize("api_request, api_key, expected_exception", validate_request_test_cases)
def test_validate_request(api_request, api_key, expected_exception):
    """Test the validate_request function with various scenarios."""
    if expected_exception:
        with pytest.raises(HTTPException) as exc_info:
            validate_request(api_request, api_key)
        assert exc_info.value.status_code == expected_exception.status_code
        assert exc_info.value.detail == expected_exception.detail
    else:
        try:
            validate_request(api_request, api_key)
        except HTTPException:
            pytest.fail("validate_request() raised HTTPException unexpectedly!")
