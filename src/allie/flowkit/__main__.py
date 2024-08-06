"""Main module for the FlowKit service."""
try:
    import uvicorn
except ImportError:
    raise ImportError(
        "Please install uvicorn to run the service: pip install allie-flowkit-python[all]"
    )
import argparse


def main():
    """Run entrypoint for the FlowKit service."""
    parse  = argparse.ArgumentParser()
    parse.add_argument("--host", type=str, default="0.0.0.0", help="The host to run the service on. By default 0.0.0.0")
    parse.add_argument("--port", type=int, default=8000, help="The port to run the service on. By default 8000")
    parse.add_argument("--workers", type=int, default=4, help="The number of workers to use. By default 4")
    args = parse.parse_args()
    uvicorn.run("allie.flowkit:flowkit_service", host=args.host, port=args.port, workers=args.workers)


if __name__ == "__main__":
    main()
