import os
import pprint
from common_lib.common import Common
from common_lib.environment import Environment

class TestBackupsNoTemplate:

    instance_env = None

    @classmethod
    def setup_class(cls):
        """
        setup state specific to the execution of tests in this class
        """
        try:
            cls.instance_env = Environment()
            print("Reading Clients payload")

        except Exception as ex:
            print(ex)

    def test_backup_valid_without_template(self):
        print("\n======================================")
        print("In test: test_backup_valid_without_template")
        print("======================================")
        try:
            client_payload_path = os.path.join(Common.get_project_path(),
                                               "src", "test_data", "api",
                                               "vm_backup.json")
            # option1: use static payload
            # payload = Common.read_json_file(client_payload_path)
            # print(f"\n Payload : {payload} \n")

            # option2: use dynamic values from env file
            vmware_win_client_details = self.instance_env.get_vmware_windows_details()
            payload = Common.read_json_file(client_payload_path)
            payload["hypervisor_info"]["esx_ip"] = vmware_win_client_details["vmware_server_ip"]
            payload["hypervisor_info"]["username"] = vmware_win_client_details['vmware_username']
            payload["hypervisor_info"]["password"] = vmware_win_client_details['vmware_password']
            payload["vm_info"]["name"] = vmware_win_client_details['win_vm_name']
            payload["vm_info"]["vm_ip"] = vmware_win_client_details['win_vm_ip_address']
            payload["vm_info"]["username"] = vmware_win_client_details['win_vm_username']
            payload["vm_info"]["password"] = vmware_win_client_details['win_vm_password']

            pprint.PrettyPrinter().pprint(payload)

            # Send the POST request
            # response = requests.post(endpoint, headers=headers, json=payload)
        except Exception as ex:
            print(ex)

    def test_backup_invalid_without_template(self):
        print("\n======================================")
        print("In test: test_backup_invalid_without_template")
        print("======================================")
        try:
            client_payload_path = os.path.join(Common.get_project_path(),
                                               "src", "test_data", "api",
                                               "vm_backup.json")
            payload = Common.read_json_file(client_payload_path)
            payload["vm_info"]["vm_ip"] = "256.256.256.256"
            pprint.PrettyPrinter().pprint(payload)

            # Send the POST request
            # response = requests.post(endpoint, headers=headers, json=payload)
            # change ip to win_ip in json and test
            # payload impacted



        except Exception as ex:
            print(ex)
