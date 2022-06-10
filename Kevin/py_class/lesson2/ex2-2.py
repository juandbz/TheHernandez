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
    print(ssh.find_prompt())
    ver_output = ssh.send_command("show cdp neighbors detail", use_textfsm=True)
    print(ver_output[0]["local_port"]) #to select a section.
        