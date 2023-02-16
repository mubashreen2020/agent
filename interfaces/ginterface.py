import psutil
import socket
import pymongo
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

    # Connect to the local MongoDB database
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["reach_manage"]
    collection = db["interface"]
    
    # Connect to the MongoDB database
    cloudclient = pymongo.MongoClient("mongodb+srv://mj:Mujff%40r@reachmanage.fsjfoer.mongodb.net/?retryWrites=true&w=majority")
    clouddb = cloudclient["reach_manage"]
    cloudcollection = clouddb["interface"]

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

            # Insert the information into the MongoDB database
            collection.insert_one({
                "interfaces": interface_name,
                "public_ip": public_ip,
                "types": types,
                "ipv4a": ipv4a
            })
            # Insert the information into the MongoDB database
            cloudcollection.insert_one({
                "interfaces": interface_name,
                "public_ip": public_ip,
                "types": types,
                "ipv4a": ipv4a
            })

# Insert the information about the network interfaces into the MongoDB database
get_network_info()
