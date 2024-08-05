try:
    import uvicorn
except ImportError:
    raise ImportError("Please install uvicorn to run the service: pip install allie-flowkit-python[all]")

from allie.flowkit.flowkit_service import flowkit_service


def main():
    uvicorn.run("allie.flowkit:flowkit_service", host="0.0.0.0", port=8000, workers=4)

if __name__ == "__main__":
    main()