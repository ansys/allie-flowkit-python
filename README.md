# Allie PyFlowKit

Welcome to the **Allie PyFlowKit** repository! This repository hosts Python functions similar to the [Allie FlowKit](https://github.com/ansys/allie-flowkit) and serves as a service to expose APIs for each individual external function added to it. These functions can be used to build Allie workflows, enabling a flexible and modular approach to creating and executing workflows with Allie.

## Table of Contents
- [Introduction](#introduction)
- [Purpose](#purpose)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Adding Custom Functions](#adding-custom-functions)
- [Example Functions](#example-functions)
- [Contributing](#contributing)

## Introduction

**Allie PyFlowKit** is designed to host the code for a Python service that exposes REST APIs for each external function added to it. These functions can be seamlessly integrated into Allie workflows and executed by the Allie Agent, making it easier for teams to customize and extend their workflow capabilities.

## Purpose

The main purpose of this repository is to:
1. Host Python functions similar to those in the [Allie FlowKit](https://github.com/ansys/allie-flowkit).
2. Provide a service that exposes these functions as REST APIs.
3. Enable the creation of custom Allie workflows using these functions.
4. Allow other teams to add their needed functions to support their specific Allie workflows.

## How It Works

1. **Function Integration:** External functions are added to this repository and exposed as REST APIs.
2. **Workflow Execution:** Allie workflows can include functions from Allie PyFlowKit.
3. **API Calls:** When an Allie workflow includes a function from Allie PyFlowKit, the Allie Agent calls the function via REST API with the required inputs.
4. **Function Execution:** The function is executed in Allie PyFlowKit, and the output is returned as the body of the REST response.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A running instance of the Allie Toolkit

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/allie-flowkit-python.git
    cd allie-flowkit-python
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Start the service:
    ```sh
    python ./app/app.py
    ```

2. The service will expose the functions as REST APIs on the specified port (default: 5000).

3. Integrate these APIs into your Allie workflows as needed.

## Adding Custom Functions

1. **Create a New Function:**
   - Add your function code to a new Python file in the `functions` directory.
   
2. **Register the Function:**
   - Import and register your function in `app.py` to expose it as a REST API.

3. **Example:**
   ```python
   from flask import Flask, request, jsonify
   from functions import my_custom_function

   app = Flask(__name__)

   @app.route('/my_custom_function', methods=['POST'])
   def my_custom_function_route():
       input_data = request.json
       result = my_custom_function(input_data)
       return jsonify(result)

   if __name__ == '__main__':
       app.run(port=5000)
   ```

## Example Functions

The repository includes some standard functions prefilled by the Allie team. You can use these as references or starting points for adding your own custom functions.

## Contributing

We welcome contributions from all teams. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push your branch to your fork.
4. Open a pull request to merge your changes into the main repository.

---

Thank you for using Allie PyFlowKit! We hope this repository helps you create powerful and flexible Allie workflows. Happy coding!
