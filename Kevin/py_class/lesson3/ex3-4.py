import json
from pprint import pprint

with open('ex3-4.json') as f:
    file = json.load(f)

ip_key = file["ipV4Neighbors"]
values ={}

for key in ip_key:
    add_key = key["address"]
    mac_key = key["hwAddress"]
    values['ip']= add_key
    values['mac'] = mac_key
    print()
    pprint(values)