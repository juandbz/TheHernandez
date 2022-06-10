#creating vlans forom vlan file.
from netmiko import ConnectHandler

Nexus1 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.32",
    "username": "kevin",
    "password": "kevin"
}
Nexus2 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.38",
    "username": "kevin",
    "password": "kevin"
}
for n in (Nexus1, Nexus2):
    ssh = ConnectHandler(**n)
    print(ssh.send_config_from_file("vlan.txt"))
    print(ssh.save_config())
    