import docker
import random
import string
import time
import json

class InstantboxManager(object):
    CONTAINER_PREFIX = 'instantbox_managed_'
    TIMEOUT_LABEL = 'org.instantbox.variables.EXPIRATION_TIMESTAMP'
    OS_LIST = None

    def __init__(self):
        self.client = docker.from_env()

        try:
            with open('manifest.json', 'r') as os_manifest:
                self.OS_LIST = json.load(os_manifest)
        except Exception:
            pass

        if self.OS_LIST is None:
            raise Exception(
                'Could not load manifest.json. ' +
                'Download it from https://get.instantbox.org/manifest.json'
            )

        self.AVAILABLE_OS_LIST = []
        for os in self.OS_LIST:
            for ver in os['subList']:
                self.AVAILABLE_OS_LIST.append(ver['osCode'])

    def is_create_container(self,
                            mem,
                            cpu,
                            os_name,
                            os_timeout,
                            open_port=None):
        # (Same as before)

    def get_container_ports(self, container_name):
        # (Same as before)

    def remove_timeout_containers(self):
        # (Same as before)

    def is_rm_container(self, container_id) -> bool:
        # (Same as before)

    def is_os_available(self, osCode=None) -> bool:
        # (Same as before)

    def generateContainerName(self) -> str:
        # (Same as before)

if __name__ == '__main__':
    while True:
        test = InstantboxManager()
        container_name = test.is_create_container('512', 1,
                                                  'instantbox/ubuntu:latest',
                                                  time.time())
        test.get_container_ports(container_name)
        test.remove_timeout_containers()
        test.is_rm_container(container_name)
        
        # Check for an exit condition (e.g., after a certain number of iterations)
        if some_exit_condition:
            break  # Exit the loop
        
        time.sleep(60)  # Sleep for 60 seconds before the next iteration
