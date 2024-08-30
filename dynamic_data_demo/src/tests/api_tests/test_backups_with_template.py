import os
import pprint

from common_lib.common import Common
from common_lib.environment import Environment
from common_lib.template_processor import JsonTemplateProcessor


class TestsBackupsWithTemplates:
    instance_env = None
    client_template = None

    @classmethod
    def setup_class(cls):
        """
        setup state specific to the execution of tests in this class
        """
        try:
            cls.instance_env = Environment()
            print("Reading Clients payload template")
            client_payload_path = os.path.join(Common.get_project_path(),
                                               "src", "test_data", "api",
                                               "vm_backup_with_template.json")
            cls.client_template = JsonTemplateProcessor(client_payload_path)
        except Exception as ex:
            print(ex)

    def test_backup_post_with_template(self):
        print("\n======================================")
        print("In test: test_backup_post_with_template")
        print("======================================")
        try:
            vmware_win_client_details = self.instance_env.get_vmware_windows_details()

            win_client_details = {"esx_server_ip": vmware_win_client_details['vmware_server_ip'],
                                    "esx_username": vmware_win_client_details['vmware_username'],
                                    "esx_password": vmware_win_client_details['vmware_password'],
                                    "name_of_vm_to_backup": vmware_win_client_details['win_vm_name'],
                                    "vm_ip": vmware_win_client_details['win_vm_ip_address'],
                                    "vm_username": vmware_win_client_details['win_vm_username'],
                                    "vm_password": vmware_win_client_details['win_vm_password']}
            filled_clients_payload = self.client_template.fill_template_json(win_client_details)
            pprint.PrettyPrinter().pprint(filled_clients_payload)

            # Send the POST request
            # response = requests.post(endpoint, headers=headers, json=payload)
        except Exception as ex:
            print(ex)

    def test_backup_post_invalid_ip_with_template(self):
        print("\n======================================")
        print("In test: test_backup_post_invalid_ip_with_template")
        print("======================================")
        try:
            vmware_win_client_details = self.instance_env.get_vmware_windows_details()

            win_client_details = {"esx_server_ip": vmware_win_client_details['vmware_server_ip'],
                                    "esx_username": vmware_win_client_details['vmware_username'],
                                    "esx_password": vmware_win_client_details['vmware_password'],
                                    "name_of_vm_to_backup": vmware_win_client_details['win_vm_name'],
                                    "vm_ip": "256.256.256.256",
                                    "vm_username": vmware_win_client_details['win_vm_username'],
                                    "vm_password": vmware_win_client_details['win_vm_password']}
            filled_clients_payload = self.client_template.fill_template_json(win_client_details)
            pprint.PrettyPrinter().pprint(filled_clients_payload)
            # change ip to win_ip in json and test
            # payload not impacted

            # Send the POST request
            # response = requests.post(endpoint, headers=headers, json=payload)
        except Exception as ex:
            print(ex)
