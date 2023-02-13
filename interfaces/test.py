import mongodb_connection

def save_interface_info(interface_data_list):
    # Insert the list of interface data into the MongoDB collection
    mongodb_connection.collection.insert_many(interface_data_list)

# Example usage
interface_data_list = [
    {
        "name": "eth0",
        "type": "Ethernet",
        "ipv4_address": "192.168.1.100",
        "public_ip": "100.100.100.100"
    },
    {
        "name": "eth1",
        "type": "Ethernet",
        "ipv4_address": "192.168.1.101",
        "public_ip": "100.100.100.101"
    }
]
save_interface_info(interface_data_list)
