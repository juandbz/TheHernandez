from time import time
from netmiko import ConnectHandler
import time 
Nexus1 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.32",
    "username": "kevin",
    "password": "kevin",
    "session_log": "my_output.txt"
}
Nexus2 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.38",
    "username": "kevin",
    "password": "kevin",
    "session_log": "my_output.txt"
}
for n in (Nexus1, Nexus2):
    ssh = ConnectHandler(**n)
    print(ssh.send_config_from_file("vlan.txt"))
    print(ssh.find_prompt())
    print(ssh.config_mode())
    print(ssh.find_prompt())
    print(ssh.exit_config_mode())
    print(ssh.find_prompt())
    print(ssh.write_channel("disable\n"))
    time.sleep(2)
    print(ssh.read_channel()) 
    print(ssh.enable())
    print(ssh.find_prompt())
    ssh.disconnect()
