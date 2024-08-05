from typing import List

from allie.flowkit.config._config import CONFIG
from allie.flowkit.endpoints import splitter
from allie.flowkit.fastapi_utils import extract_endpoint_info
from allie.flowkit.models.functions import EndpointInfo
from fastapi import FastAPI, Header, HTTPException

flowkit_service = FastAPI()

# Include routers from all endpoints
flowkit_service.include_router(splitter.router, prefix="/splitter", tags=["splitter"])

# Map of function names to function objects
function_map = {
    "split_ppt": splitter.split_ppt,
    "split_pdf": splitter.split_pdf,
    "split_py": splitter.split_py,
}


# Endpoint to list all enpoint information
@flowkit_service.get("/", response_model=List[EndpointInfo])
async def list_functions(api_key: str = Header(...)) -> List[EndpointInfo]:
    """List all available functions and their endpoints.

    Parameters
    ----------
    api_key : str
        The API key for authentication.

    Returns
    -------
    List[EndpointInfo]
        A list of EndpointInfo objects representing the endpoints.

    """
    # Check if the API key is valid
    if api_key != CONFIG.flowkit_python_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return extract_endpoint_info(function_map, flowkit_service.routes)
