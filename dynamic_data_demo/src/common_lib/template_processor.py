import json
import logging
import threading

from json_templates import JsonTemplates

'''
This class is used to process JSON templates. 
It has methods to load and fill the JSON templates with the data provided.
This is used to replace the values in input JSON files for given APIs.
'''


class JsonTemplateProcessor:
    _lock = threading.Lock()  # Lock for thread safety

    def __init__(self, template_file_path):
        self.template_file_path = template_file_path
        self.template_obj = JsonTemplates()
        self.template = None

    '''
    This method is used to load the JSON template file.
    '''

    def load_template(self):
        with self._lock:  # Use lock to ensure thread-safe loading
            try:
                self.template = self.template_obj.load(self.template_file_path)
            except FileNotFoundError:
                raise FileNotFoundError(f"Template file not found: {self.template_file_path}")
            except Exception as e:
                raise Exception(f"Error processing JSON template: {e}")

    '''
    This method is used to fill the JSON template with the data provided.
    :param
    data: Dictionary containing the data to be filled in the template
    :return
    filled_template_json: JSON template dictionary filled with the data provided
    '''

    def fill_template_json(self, data):
        self.load_template()

        with self._lock:  # Use lock to ensure thread-safe template filling
            try:
                result = self.template_obj.generate(data)
                if not result[0]:
                    logging.error(f"Error filling JSON template: {result[1]}")
                    raise Exception(f"Error filling JSON template: {result[1]}")
                filled_template = json.dumps(result[1])
                filled_template_json = json.loads(filled_template)
                return filled_template_json
            except json.JSONDecodeError as je:
                raise Exception(f"JSONDecodeError: {je}")
            except Exception as e:
                raise Exception(f"Error filling JSON template: {e}")
