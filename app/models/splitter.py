from pydantic import BaseModel
from typing import List

class SplitterRequest(BaseModel):
    text: bytes
    chunk_size: int
    chunk_overlap: int

class SplitterResponse(BaseModel):
    chunks: List[str]