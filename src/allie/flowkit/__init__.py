"""App package responsible for creating the FastAPI app."""
import importlib.metadata as importlib_metadata

__version__ = importlib_metadata.version(__name__.replace(".", "-"))

from allie.flowkit.flowkit_service import flowkit_service
