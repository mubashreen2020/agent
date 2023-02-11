import os
import re

def connect_to_openvpn():
    # Connect to OpenVPN server
    os.system("openvpn --config /etc/openvpn/server/server.conf")

    # Retrieve OpenVPN status information
    output = os.popen("openvpn --status /var/log/openvpn/openvpn.log 10").read()

    # Extract relevant information from the output
    lines = output.split("\n")
    client_list = []
    for line in lines:
        match = re.search("(.*),(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}),(\d+),(\d+),(\d+)", line)
        if match:
            client_list.append(match.groups())

    return client_list

print(connect_to_openvpn())
