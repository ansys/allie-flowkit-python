# Allie FlowKit Python

Welcome to the **Allie FlowKit Python** repository! This repository hosts Python functions similar to the [Allie FlowKit](https://github.com/ansys/allie-flowkit) and serves as a service to expose APIs for each individual external function added to it. These functions can be used to build Allie workflows, enabling a flexible and modular approach to creating and executing workflows with Allie.

## Table of Contents
- [Introduction](#introduction)
- [Purpose](#purpose)
- [How It Works](#how-it-works)
- [Run locally](#run-locally)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Run as a Docker container](#run-as-a-docker-container)
- [Adding Custom Functions](#adding-custom-functions)
- [Example Functions](#example-functions)
- [Contributing](#contributing)

## Introduction

**Allie FlowKit Python** is designed to host the code for a Python service that exposes REST APIs for each external function added to it. These functions can be seamlessly integrated into Allie workflows and executed by the Allie Agent, making it easier for teams to customize and extend their workflow capabilities.

## Purpose

The main purpose of this repository is to:
1. Host Python functions similar to those in the [Allie FlowKit](https://github.com/ansys/allie-flowkit).
2. Provide a service that exposes these functions as REST APIs.
3. Enable the creation of custom Allie workflows using these functions.
4. Allow other teams to add their needed functions to support their specific Allie workflows.

## How It Works

1. **Function Integration:** External functions are added to this repository and exposed as REST APIs.
2. **Workflow Execution:** Allie workflows can include functions from Allie FlowKit Python.
3. **API Calls:** When an Allie workflow includes a function from Allie FlowKit Python, the Allie Agent calls the function via REST API with the required inputs.
4. **Function Execution:** The function is executed in Allie FlowKit Python, and the output is returned as the body of the REST response.

## Run locally

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A running instance of the Allie Toolkit

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
    uvicorn app.app:app --host 0.0.0.0 --port 50052 --workers 1
    ```
    You can specify the host, port, and number of workers as needed.

2. The service will expose the functions as REST APIs on the specified port (default: 8000).

3. Integrate these APIs into your Allie workflows as needed.

## Run as a Docker container

1. Build the Docker container image with the following command:

```bash
    docker build -f docker/Dockerfile . -t allie-flowkit-python:latest
```

2. Run the Docker container and expose the port on your desired endpoint. You can also specify the number of workers as needed:

```bash
    docker run -d -e WORKERS=5 --rm --name allie-flowkit-python -p 50052:50052 allie-flowkit-python:latest
```

## Adding Custom Functions

1. **Create a New Function:**
   - Add your function code as an endpoint to a new Python file in the `app/endpoints` directory.
   Use the `app/endpoints/splitter.py` file and its endpoints as an example.
   Be explicit about the input and output of the function, as this will be used by the Allie Agent to call the function.

2. **Add the models for the function:**
   - Add the models for the input and output of the function in the `app/models` directory.
   Use the `app/models/splitter.py` file its models as an example.

2. **Add the endpoints to the service:**
   - Import your module in the `app/app.py` file and add the router to the service.
   ```python
   app.include_router(
       custom_endpoint.router, prefix="/custom_endpoint", tags=["custom_endpoint"]
   )
   ```

3. **Add the function to the function map:**
    - Add your function to the `function_map` dictionary in the `app/app.py` file.
    ```python
    function_map = {
        "split_ppt": splitter.split_ppt,
        "split_pdf": splitter.split_pdf,
        "split_py": splitter.split_py,
        "custom_function": custom_endpoint.custom_function,
    }
    ```

4. **Example:**
    - Create a new file in the `app/endpoints` directory for your function.
    For example, create a file named `custom_endpoint.py`.
    Add your first function to the file. Remember that it's important to explicitly define the input and output of the function. Both must be defined as Pydantic models in the `app/models` directory.

    The `custom_endpoint.py` file should look like this:
    ```python
    from fastapi import FastAPI, APIRouter
    from app.models.custom_model import CustomRequest, CustomResponse

    app = FastAPI()
    router = APIRouter()


    @router.post("/custom_function", response_model=CustomResponse)
    async def custom_function(request: CustomRequest) -> CustomResponse:
        """Endpoint for custom function.

        Parameters
        ----------
        request : CustomRequest
            An object containing the input data required for the function.

        Returns
        -------
        CustomResponse
            An object containing the output data of the function.

        """
        # Your custom processing logic here
        result = ...
        return result
    ```

    While the `app/models/custom_model.py` file should look like this:
    ```python
    from pydantic import BaseModel


    class CustomRequest(BaseModel):
        """Model for the input data required for the custom function.

        Parameters
        ----------
        BaseModel : pydantic.BaseModel
            The base model for the request.

        """

        input_data: str


    class CustomResponse(BaseModel):
        """Model for the output data of the custom function.

        Parameters
        ----------
        BaseModel : pydantic.BaseModel
            The base model for the response.

        """

        output_data: str
    ```

    - After adding the function and models, import the module in the `app/app.py` file and add the router to the service. The ``app/app.py`` file should look like this:
    ```python
    from app.endpoints import custom_endpoint

    app.include_router(splitter.router, prefix="/splitter", tags=["splitter"])
    app.include_router(
        custom_endpoint.router, prefix="/custom_endpoint", tags=["custom_endpoint"]
    )
    ```

    - Finally, every time you add a new function, you need to add it to the ``function_map`` dictionary in the ``app/app.py`` file. The ``function_map`` dictionary should look like this:
    ```python
    function_map = {
        "split_ppt": splitter.split_ppt,
        "split_pdf": splitter.split_pdf,
        "split_py": splitter.split_py,
        "custom_function": custom_endpoint.custom_function,
    }
    ```

## Example Functions

The repository includes some standard functions prefilled by the Allie team. You can use these as references or starting points for adding your own custom functions.

## Contributing

We welcome contributions from all teams. To contribute:

1. Clone the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push your branch to the repository.
4. Open a pull request to merge your changes into the main repository.

---

Thank you for using Allie FlowKit Python! We hope this repository helps you create powerful and flexible Allie workflows. Happy coding!
