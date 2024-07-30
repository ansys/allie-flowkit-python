from typing import List

from pydantic import BaseModel


class SplitterRequest(BaseModel):
    document_content: bytes
    chunk_size: int
    chunk_overlap: int


class SplitterResponse(BaseModel):
    chunks: List[str]
