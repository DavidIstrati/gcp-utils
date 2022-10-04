from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from tqdm.auto import tqdm

import requests
import time


def stop_vm(timeout: int = 60):
    """
    Stops the vm after a number of seconds
    :type timeout: integer, number of seconds before the vm closes
    """

    if timeout < 1:
        raise ValueError("Parameter \"timeout\" must be positive")

    if timeout:
        print(f"Terminating instance in {timeout} seconds!")
        for _ in tqdm(range(timeout)):
            time.sleep(1)

    credentials = GoogleCredentials.get_application_default()

    service = discovery.build('compute', 'v1', credentials=credentials)

    metadata_server = "http://metadata/computeMetadata/v1/instance/"
    metadata_flavor = {'Metadata-Flavor': 'Google'}
    project_id = requests.get(metadata_server + 'project-id', headers=metadata_flavor).text
    instance_id = requests.get(metadata_server + 'id', headers=metadata_flavor).text
    zone = requests.get(metadata_server + 'zone', headers=metadata_flavor).text
    zone = zone[zone.rindex('/') + 1:]

    request = service.instances().stop(project=project_id, zone=zone, instance=instance_id)
    request.execute()