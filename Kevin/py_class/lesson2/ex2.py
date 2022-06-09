from netmiko import ConnectHandler

Nexus1 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.32",
    "username": "kevin",
    "password": "kevin",
    "fast_cli": True
}

Nexus2 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.38",
    "username": "kevin",
    "password": "kevin",
    "fast_cli": True
}
for n in (Nexus1, Nexus2):
    ssh = ConnectHandler(**n)
    ipv4 = "8.8.8.8"
    output = ssh.send_command("ping", expect_string=r"Vrf", strip_prompt=False, strip_command=False)
    output += ssh.send_command("management", expect_string=r"Target", strip_prompt=False, strip_command=False)
    output += ssh.send_command(ipv4, expect_string=r"Repeat", strip_prompt=False, strip_command=False)
    output += ssh.send_command("10", expect_string=r"Packet", strip_prompt=False, strip_command=False)
    output += ssh.send_command("\n", expect_string=r"Timeout", strip_prompt=False, strip_command=False)
    output += ssh.send_command("\n", expect_string=r"Sending", strip_prompt=False, strip_command=False)
    output += ssh.send_command("\n", expect_string=r"Extended", strip_prompt=False, strip_command=False)
    output += ssh.send_command("\n", expect_string=r"Sweep", strip_prompt=False, strip_command=False)
    output += ssh.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)
    ssh.disconnect()
    print(output)
 
