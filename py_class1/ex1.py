from netmiko import ConnectHandler

Nexus = {
    "device_type": "cisco_nxos",s
    "host": "192.168.1.32",
    "username": "kevin",
    "password": "kevin"
}

ssh = ConnectHandler(**Nexus)

print(ssh.find_prompt())