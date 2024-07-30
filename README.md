# Allie FlowKit Python

Welcome to Allie FlowKit Python. This repository hosts Python functions similar to [Allie FlowKit](https://github.com/ansys/allie-flowkit) and provides a service for exposing APIs for each external function added to it. You can use these functions to build Allie workflows, enabling a flexible and modular approach to creating and executing workflows with Allie.

## Table of contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [How it works](#how-it-works)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Adding custom functions](#adding-custom-functions)
- [Example functions](#example-functions)
- [Contributing](#contributing)

## Introduction

Allie FlowKit Python is designed to host the code for a Python service that exposes a REST API for each external function added to it. These functions can be seamlessly integrated into Allie workflows and executed by the Allie agent, making it easier for teams to customize and extend their workflow capabilities.

## Objectives

Using Allie Flowkit Python lets you achieve these key objectives:

- Host Python functions similar to those in [Allie FlowKit](https://github.com/ansys/allie-flowkit).
- Provide a service that exposes these functions as REST APIs.
- Enable the creation of custom Allie workflows using these functions.
- Allow other teams to add their needed functions to support their specific Allie workflows.

## How it works

Allie Flowkit Python supports these actions:

1. **Function integration:** Add external functions to this repository and expose them as REST APIs.
2. **Workflow execution:** Include functions from Allie FlowKit Python in Allie workflows.
3. **API calls:** When an Allie workflow includes a function from Allie FlowKit Python, the Allie agent calls the function via a REST API with the required inputs.
4. **Function execution:** The function is executed in Allie FlowKit Python, and the output is returned as the body of the REST response.

## Getting started

### Prerequisites

- Python 3.7 or later
- pip (Python package installer)
- A running instance of the Allie Flowkit

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/allie-flowkit-python.git
    cd allie-flowkit-python
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Start the service:
   ```sh
   uvicorn app.app:app --host 0.0.0.0 --port 8000 --workers 1
   ```
   You can specify the host, port, and number of workers as needed. The service exposes the functions as REST APIs on the specified port. The default is 8000.

2. Integrate these APIs into your Allie workflows as needed.

## Adding custom functions

1. **Create a function.**
   - Add your function code as an endpoint to a new Python file in the `app/endpoints` directory.
   - Use the `app/endpoints/splitter.py` file and its endpoints as an example.
   - Be explicit about the input and output of the function as they are used by the Allie agent
   to call the function.

2. **Add the models for the function.**   
   - Add the models for the input and output of the function in the `app/models` directory.
   - Use the `app/models/splitter.py` file its models as an example.
   
2. **Add the endpoints to the service.**
   
   - Import your module in the `app/app.py` file.
   - Add the router to the service:
     ```python
     app.include_router(splitter.router, prefix="/custom_module", tags=["custom_module"])
     ```

**Example**
 ```python
 from fastapi import FastAPI, APIRouter
 from app.models.custom_model import CustomRequest, CustomResponse

 app = FastAPI()
 router = APIRouter()

 @router.post('/custom_function', response_model=CustomResponse)
 async def custom_function(request: CustomRequest) -> CustomResponse:
     """Endpoint for custom function.

     Parameters
     ----------
     request : CustomRequest
        Object containing the input data required for the function.
        
     Returns
     -------
     CustomResponse
        Object containing the output data of the function.
        """
     # Your custom processing logic here
     result = ...
     return result
 ```

## Example functions

The repository includes some standard functions prefilled by the Allie team. You can use these as references or starting points for adding your own custom functions.

## Contributing

We welcome contributions from all teams. To contribute, perform these steps:

1. Clone the repository.
2. Create a branch for your feature or bug fix.
3. Commit your changes and push your branch to the repository.
4. Open a pull request to merge your changes into the main repository.

---

Thank you for using Allie FlowKit Python. We hope this repository helps you create powerful and flexible Allie workflows. Happy coding!
