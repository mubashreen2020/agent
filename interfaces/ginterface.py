import psutil
import socket
import requests



def get_network_info():
    # Get information about the network interfaces
    interfaces = psutil.net_if_addrs()

    # Loop through the network interfaces
    for interface_name, interface_addresses in interfaces.items():
        # Get the first IPv4 address of the interface
        ipv4_address = next((address.address for address in interface_addresses if address.family == socket.AF_INET), None)


def get_public_ip():
    # Make a request to a public IP address API
    response = requests.get("https://api.ipify.org")
    public_ip = response.text
    
    return public_ip

public_ip = get_public_ip()

            interfacearray = (name:interface_name,'Loopback' if interface_name == 'lo' else 'Physical',ipv4_address,public_ip)
            print(interfacearray)
            # Print the information about the interface
            print(f"Name: {interface_name}\nType: {'Loopback' if interface_name == 'lo' else 'Physical'}\nIPv4 Address: {ipv4_address}\nPublic IP: {public_ip}\n")

# Print the information about the network interfaces
get_network_info()
