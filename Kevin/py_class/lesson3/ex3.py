import re
from pprint import pprint

arp_data = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.220.88.1            67   0062.ec29.70fe  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.20           29   c89c.1dea.0eb6  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.37          104   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.38          161   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
"""
    
arp_data = arp_data.strip()# strips indents
arp_list = arp_data.splitlines()#stips the whole strings into blocks of strings
processed_list = []
for arp_entry in arp_list:
    if re.search(r"^Protocol.*Interface", arp_entry):# r"^ is the first word and everything in between the * is the last word
        continue
    _, ip_addr, _, mac_addr, _, intf = arp_entry.split()
    print(arp_entry)
    arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intf}# making a dictionary 
    processed_list.append(arp_dict)# copyed the dictionary in a list

print()
pprint(processed_list)
print()