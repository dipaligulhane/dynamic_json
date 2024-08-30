import json
import os


class Common:
    @staticmethod
    def get_project_path():

        """ Get the project path for the current file"""
        try:
            project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            return project_path
        except Exception:
            print("ERROR: Unable to get project path")
            raise Exception("Unable to get project path")

    @staticmethod
    def get_test_data_api_folder_path() -> str:
        return os.path.join(Common.get_project_path(), "src", "testdata", "api")

    @staticmethod
    def read_json_file(json_file_path: str) -> dict:
        """To convert json file to dictionary

        Args:
            json_file_path (str): path of payload file in /tests/data/

        Returns:
            (dict): JSON file in dictionary format.
        """
        try:
            with open(json_file_path) as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"ERROR: File {json_file_path} does not exist.")
            raise FileNotFoundError(f"File {json_file_path} does not exist.")
        except Exception as e:
            print(f"ERROR: Unable to read file {json_file_path}.\nException: {e}")
            raise Exception(f"Unable to read file {json_file_path}. Exception: {e}")