import yaml
from pprint import pprint

Nexus1 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.32"
}

Nexus2 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.38"
}

devices = [
    Nexus1,
    Nexus2
]
for device in devices:
    device["username"] = "kevin"
    device["password"] = "kevin"
pprint(devices)


with open('devices.yaml', 'w',) as file:
    yaml.dump(devices, file)
