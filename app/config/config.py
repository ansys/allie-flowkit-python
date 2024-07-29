import yaml
from pathlib import Path

class Config:
    """
    A class to represent the configuration settings.

    Attributes
    ----------
    flowkit_python_api_key : str
        The API key for accessing the Allie Flowkit Python service.

    Methods
    -------
    _read_config_file(config_path: str) -> dict
        Reads the YAML configuration file and returns its content as a dictionary.
    """

    def __init__(self, config_path: str):
        """
        Initializes the Config object by reading the configuration file and extracting the required API key.

        Parameters
        ----------
        config_path : str
            The path to the YAML configuration file.

        Raises
        ------
        ValueError
            If the 'FLOWKIT_PYTHON_API_KEY' is not found in the configuration file.
        """
        self.config = self._load_config(config_path)
        self.flowkit_python_api_key = self.config.get('FLOWKIT_PYTHON_API_KEY')

        if not self.flowkit_python_api_key:
            raise ValueError("FLOWKIT_PYTHON_API_KEY is missing in the configuration file.")

    def _load_config(self, config_path: str) -> dict:
        """
        Reads the YAML configuration file.

        Parameters
        ----------
        config_path : str
            The path to the YAML configuration file.

        Returns
        -------
        dict
            The content of the configuration file as a dictionary.
        """
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

# Initialize the config object
config_path = Path("config.yaml")
config = Config(config_path)
