from typing import List
from fastapi import FastAPI, HTTPException, Header

from app.endpoints import splitter
from app.fastapi_utils import extract_endpoint_info
from app.models.functions import EndpointInfo
from app.config.config import config

app = FastAPI()

# Include routers from all endpoints
app.include_router(splitter.router, prefix="/splitter", tags=["splitter"])

# Map of function names to function objects
function_map = {
    "split_ppt": splitter.split_ppt,
    "split_pdf": splitter.split_pdf,
    "split_py": splitter.split_py,
}

# Endpoint to list all enpoint information
@app.get("/", response_model=List[EndpointInfo])
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
    if api_key != config.pyflowkit_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return extract_endpoint_info(function_map, app.routes)