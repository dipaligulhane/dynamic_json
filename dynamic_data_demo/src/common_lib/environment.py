import os
import threading

import yaml

from common_lib.common import Common


class Environment:
    _instance = None
    _lock = threading.Lock()  # Lock object to ensure thread safety

    project_path = None
    env_file_path = None
    yaml_data = None

    def __new__(cls, *args, **kwargs):
        # Double-checked locking mechanism
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-check to ensure only one instance
                    cls._instance = super(Environment, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.project_path is None:  # Initialize only if not already set
            self.project_path = Common.get_project_path()
            api_config_folder_path = os.path.join(self.project_path, "src", "config", "api")
            self.env_file_path = os.path.join(api_config_folder_path, 'env_details.yaml')
            self.yaml_data = self.read_env_file()

    def read_env_file(self) -> dict:
        try:
            with open(self.env_file_path) as f:
                return yaml.safe_load(f)
        except FileNotFoundError as ef:
            print(f"ERROR: File {self.env_file_path} does not exist.\nException: {ef}")
            raise FileNotFoundError(f"File {self.env_file_path} does not exist. Exception: {ef}")
        except Exception as e:
            print(f"ERROR: Unable to read file {self.env_file_path}.\nException: {e}")
            raise Exception(f"Unable to read file {self.env_file_path}. Exception: {e}")

    def get_vmware_windows_details(self) -> dict:
        if self.yaml_data is not None:
            return self.yaml_data['client_details']['vmware_windows']
