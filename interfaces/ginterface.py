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
    response = requests.get("http://checkip.dyndns.org").text
    # Extract the public IP address from the response
    public_ip = response.split("<body>")[1].split("</body>")[0].strip()
    
    return public_ip

public_ip = get_public_ip()


# Print the information about the network interfaces
get_network_info()
