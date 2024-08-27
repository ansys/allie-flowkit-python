# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Main module for the FlowKit service."""

try:
    from allie.flowkit.config._config import CONFIG
    import uvicorn
except ImportError:
    raise ImportError("Please install uvicorn to run the service: pip install allie-flowkit-python[all]")
import argparse
from urllib.parse import urlparse


def parse_cli_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, help="The host to run the service on. By default 0.0.0.0")
    parser.add_argument("--port", type=int, help="The port to run the service on. By default 50052")
    parser.add_argument("--workers", type=int, help="The number of workers to use. By default 4")
    parser.add_argument("--use-ssl", help="Enable SSL for the service. By default False")
    parser.add_argument("--ssl-keyfile", type=str, help="The SSL key file path")
    parser.add_argument("--ssl-certfile", type=str, help="The SSL certificate file path")
    return parser.parse_args()

def substitute_empty_values(args):
    """Substitute the empty values with configuration values."""
    host = args.host or urlparse(CONFIG.flowkit_python_endpoint).hostname
    port = args.port or urlparse(CONFIG.flowkit_python_endpoint).port
    workers = args.workers or CONFIG.flowkit_python_workers
    use_ssl = (args.use_ssl.lower() == 'true') if args.use_ssl is not None else CONFIG.use_ssl
    ssl_keyfile = args.ssl_keyfile or CONFIG.ssl_cert_private_key_file
    ssl_certfile = args.ssl_certfile or CONFIG.ssl_cert_public_key_file
    return host, port, workers, use_ssl, ssl_keyfile, ssl_certfile

def main():
    """Run entrypoint for the FlowKit service."""
    # Parse the command line arguments
    args = parse_cli_args()

    # Substitute the empty values with configuration values
    host, port, workers, use_ssl, ssl_keyfile, ssl_certfile = substitute_empty_values(args)

    # Run the service
    uvicorn.run(
        "allie.flowkit.flowkit_service:flowkit_service",
        host=host,
        port=port,
        workers=workers,
        ssl_keyfile=ssl_keyfile if use_ssl else None,
        ssl_certfile=ssl_certfile if use_ssl else None,
    )


if __name__ == "__main__":
    main()
