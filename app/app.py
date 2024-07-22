from fastapi import FastAPI
from app.endpoints import splitter

app = FastAPI()

# Include routers from all endpoints
app.include_router(splitter.router, prefix="/splitter", tags=["splitter"])
