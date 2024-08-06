"""Model for the splitter endpoint."""
from typing import List

from pydantic import BaseModel


class SplitterRequest(BaseModel):
    """Request model for the splitter endpoint.

    Parameters
    ----------
    BaseModel : pydantic.BaseModel
        The base model for the request.

    """

    document_content: bytes
    chunk_size: int
    chunk_overlap: int


class SplitterResponse(BaseModel):
    """Response model for the splitter endpoint.

    Parameters
    ----------
    BaseModel : pydantic.BaseModel
        The base model for the response.

    """

    chunks: List[str]
