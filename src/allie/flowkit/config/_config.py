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

"""Module for reading the configuration settings from a YAML file."""
import os
from pathlib import Path

import yaml


class Config:
    """Represent the configuration settings.

    Attributes
    ----------
    flowkit_python_api_key : str
        The API key for accessing the Allie Flowkit Python service.

    Methods
    -------
    _load_config(config_path: str) -> dict
        Read the YAML configuration file and return its content as
        a dictionary.

    """

    def __init__(self):
        """Initialize the Config object by reading the configuration file.

        Also, check if the 'FLOWKIT_PYTHON_API_KEY' is present in the
        configuration file.

        Raises
        ------
        ValueError
            If the 'FLOWKIT_PYTHON_API_KEY' is not found in the
            configuration file.

        """
        config_path = os.getenv("ALLIE_CONFIG_PATH", "config.yaml")
        self._yaml = self._load_config(config_path)
        self.flowkit_python_api_key = self._yaml.get("FLOWKIT_PYTHON_API_KEY")

        if not self.flowkit_python_api_key:
            raise ValueError("FLOWKIT_PYTHON_API_KEY is missing in the configuration file.")

    def _load_config(self, config_path: str) -> dict:
        """Read the YAML configuration file.

        Parameters
        ----------
        config_path : str
            The path to the YAML configuration file.

        Returns
        -------
        dict
            The content of the configuration file as a dictionary.

        Raises
        ------
        FileNotFoundError
            If the configuration file is not found at the given path.

        """
        try:
            with Path(config_path).open("r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Configuration file not found at: {config_path}, using default location.")
            try:
                with Path("configs/config.yaml").open("r") as file:
                    return yaml.safe_load(file)
            except FileNotFoundError:
                try:
                    with Path("../../configs/config.yaml").open("r") as file:
                        return yaml.safe_load(file)
                except FileNotFoundError:
                    raise FileNotFoundError("Configuration file not found at the default location.")

# Initialize the config object
CONFIG = Config()
