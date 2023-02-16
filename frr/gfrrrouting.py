import pymongo
import subprocess

def get_frr_routing_table():
    # Run the frr CLI command to get the routing table information
    output = subprocess.check_output(["vtysh", "-c", "show ip route"]).decode("utf-8")
    # Split the output into lines
    lines = output.split("\n")
    # Initialize a list to store the routing table entries
    entries = []
    # Loop through the lines
    for line in lines:
        # Split the line into columns
        columns = line.split()
        # If the line contains information about a routing table entry
        if len(columns) >= 6:
            # Extract the desired information from the columns
            destination = columns[0]
            gateway = columns[1]
            metric = columns[2]
            protocol = columns[4]
            interface = columns[5]
            # Append the routing table entry to the list of entries
            entries.append({
                "destination": destination,
                "gateway": gateway,
                "metric": metric,
                "protocol": protocol,
                "interface": interface
            })
    # Return the list of routing table entries
    return entries

def save_routing_table_to_mongodb():
    # Get the routing table information
    routing_table = get_frr_routing_table()
    # Connect to the MongoDB database
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["reach_manage"]
    collection = db["frrrouting"]
    # Insert the routing table entries into the MongoDB database
    for entry in routing_table:
        collection.insert_one(entry)

# Call the function to save the routing table in the MongoDB database
save_routing_table_to_mongodb()
