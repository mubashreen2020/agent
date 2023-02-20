import pymongo
import subprocess

def get_frr_routing_table():
    # Run the frr CLI command to get the routing table information
    output = subprocess.check_output(["vtysh", "-c", "show ip route"]).decode("utf-8")
    # Split the output into lines
    lineso = output.split("\n")
   # print(lineso)
    lines = lineso[7:]
    print(lines)
    linesn = lines[:-1]
    print(linesn)
    # Initialize a list to store the routing table entries  
    entries = []
    # Loop through the lines
    for line in linesn:
        # Split the line into columns
        columns = line.split()
        print(columns)
        # If the line contains information about a routing table entry
        dummy = columns[0]
        print(dummy)
        if 'K>*' in dummy :
        
            # Extract the desired information from the columns
            gateway = columns[4]
            #print(gateway)
            destination = columns[1]
            metric = columns[2]
            protocol = columns[0]
            interface = columns[5]
            # Append the routing table entry to the list of entries
            
        elif 'K' in dummy :
                    # Extract the desired information from the columns
            gateway = columns[5]
            #print(gateway)
            destination = columns[2]
            metric = columns[3]
            protocol = columns[0]
            interface = columns[6]
            # Append the routing table entry to the list of entries
            
           
        elif 'C>*' in dummy :
                    # Extract the desired information from the columns
            gateway = columns[3]
            #print(gateway)
            destination = columns[1]
            metric = columns[3]
            protocol = columns[0]
            interface = columns[5]
           
        elif 'C' in dummy :
                    # Extract the desired information from the columns
            gateway = columns[4]
            #print(gateway)
            destination = columns[2]
            metric = columns[4]
            protocol = columns[0]
            interface = columns[6]
            # Append the routing table entry to the list of entries
            
        entries.append({
                "gateway": gateway,
                "destination": destination,
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
