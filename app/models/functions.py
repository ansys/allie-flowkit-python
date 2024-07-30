from typing import Any, Dict, List

from pydantic import BaseModel


class ParameterInfo(BaseModel):
    name: str
    type: str


class EndpointInfo(BaseModel):
    name: str
    path: str
    inputs: List[ParameterInfo]
    outputs: List[ParameterInfo]
    definitions: Dict[str, Any]
