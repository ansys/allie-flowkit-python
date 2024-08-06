"""Module for defining the models used in the endpoints."""
from typing import Any, Dict, List

from pydantic import BaseModel


class ParameterInfo(BaseModel):
    """Parameter information model.

    Parameters
    ----------
    BaseModel : pydantic.BaseModel
        The base model for the parameter information

    """

    name: str
    type: str


class EndpointInfo(BaseModel):
    """Endpoint information model.

    Parameters
    ----------
    BaseModel : pydantic.BaseModel
        The base model for the endpoint information

    """

    name: str
    path: str
    inputs: List[ParameterInfo]
    outputs: List[ParameterInfo]
    definitions: Dict[str, Any]
