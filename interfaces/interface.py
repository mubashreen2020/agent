from flask import Flask, jsonify
from pymongo import MongoClient
import socket
import requests
import psutil

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient("mongodb+srv://mj:FsR47oq0d2OjwXkt@cluster0.cc99ozj.mongodb.net/test")
db = client["network_info"]
collection = db["interfaces"]

@app.route('/interfaces', methods=['GET'])
def get_interfaces():
    # Get information about the network interfaces
    interfaces = psutil.net_if_addrs()

    # List to store the interface information
    interface_list = []

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

            # Add the interface information to the list
            interface_list.append({
                'interface_name': interface_name,
                'public_ip': public_ip,
                'types': types,
                'ipv4a': ipv4a
            })

    # Save the interface information to the MongoDB database
    collection.insert_many(interface_list)

    # Return the interface information as a JSON response
    return jsonify(interface_list)

def get_public_ip():
    # Make a request to a public IP address API
    response = requests.get("http://checkip.dyndns.org").text
    # Extract the public IP address from the response
    public_ip = response.split("<body>")[1].split("</body>")[0].strip()
    
    return public_ip

if __name__ == '__main__':
    app.run()
