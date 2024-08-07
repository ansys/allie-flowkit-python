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
