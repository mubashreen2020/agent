import psutil
import socket
import mongodb_connection
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
            types = 'Loopback' if interface_name == 'lo' else 'Physical'
            ipv4a = ipv4_address
            interfaceprint = names+interface_name+typee+types+ipv4+ipv4a+f'"'

# insert the data into the collection
mongodb_connection.collection.insert_many({
    
    "public_ip": public_ip,
    "name": interface_name,
    "type": types,
    "ipv4_address": ipv4a
})

# Confirm the data has been inserted
print(mongodb_connection.collection.count_documents({}))

# Print the information about the network interfaces
get_network_info()
