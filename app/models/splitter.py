from pydantic import BaseModel
from typing import List

class SplitterRequest(BaseModel):
    document_content: bytes
    chunk_size: int
    chunk_overlap: int

class SplitterResponse(BaseModel):
    chunks: List[str]