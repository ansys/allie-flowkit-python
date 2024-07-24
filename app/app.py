from typing import List
from fastapi import FastAPI

from app.endpoints import splitter
from app.fastapi_utils import extract_endpoint_info
from app.models.functions import EndpointInfo

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
async def list_functions() -> List[EndpointInfo]:
    return extract_endpoint_info(function_map, app.routes)