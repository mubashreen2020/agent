import psutil
import socket
import requests

def get_public_ip():
    # Make a request to a public IP address API
    response = requests.get("http://checkip.dyndns.org").text
    # Extract the public IP address from the response
    public_ip = response.split("<body>")[1].split("</body>")[0].strip()
    
    return public_ip

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
            public_ip = get_public_ip()
            
            space =f' '
            equalto= f'="'
            names = f'"Name":'
            typee = f'","Type":'
            types = 'Loopback' if interface_name == 'lo' else 'Physical'
            ipv4 = f'","IPv4 Address":'
            ipv4a = ipv4_address
            interfaceprint = names+equalto+space+interface_name+space+typee+equalto+space+types+space+ipv4+equalto+space+ipv4a+space

            # Print the information about the interface
            print(f"{interfaceprint}\n")

# Print the information about the network interfaces
get_network_info()
