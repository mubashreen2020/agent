import netifaces

# Retrieve a list of network interfaces and their associated MAC addresses
interfaces = netifaces.interfaces()
for interface in interfaces:
    if interface != 'lo':
        mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
        print(f"Interface {interface} has MAC address {mac_address}")
