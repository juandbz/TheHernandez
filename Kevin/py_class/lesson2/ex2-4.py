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
command1 =["ip name-server 8.8.8.8 use-vrf management",
        "ip name-server 8.8.4.4 use-vrf management",
        "ip domain-lookup",
]
ping ="ping 8.8.8.8 vrf management"

for n in (Nexus1, Nexus2):
    ssh = ConnectHandler(**n)
    print(ssh.send_command(ping))
    print(ssh.send_config_set(command1))
    print(ssh.find_prompt())
    