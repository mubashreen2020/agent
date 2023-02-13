import psutil
import socket

def get_network_info():
    # Get information about the network interfaces
    interfaces = psutil.net_if_addrs()

    # Loop through the network interfaces
    for interface_name, interface_addresses in interfaces.items():
        # Get the first IPv4 address of the interface
        ipv4_address = next((address.address for address in interface_addresses if address.family == socket.AF_INET), None)

        # If the interface has an IPv4 address
        if ipv4_address:
            # Get the public IP address
            public_ip = socket.gethostbyname(socket.gethostname())

            interfacearray = (interface_name,{'Loopback' if interface_name == 'lo' else 'Physical'},{ipv4_address},{public_ip})
            print(interfacearray)
            # Print the information about the interface
            print(f"Name: {interface_name}\nType: {'Loopback' if interface_name == 'lo' else 'Physical'}\nIPv4 Address: {ipv4_address}\nPublic IP: {public_ip}\n")

# Print the information about the network interfaces
get_network_info()
