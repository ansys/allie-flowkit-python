from pydantic import BaseModel
from typing import List, Dict, Any

class ParameterInfo(BaseModel):
    name: str
    type: str

class EndpointInfo(BaseModel):
    name: str
    path: str
    inputs: List[ParameterInfo]
    outputs: List[ParameterInfo]
    definitions: Dict[str, Any]