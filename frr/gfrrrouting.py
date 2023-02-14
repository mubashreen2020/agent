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
            protocal = columns[4]
            interface = columns[5]
            # Append the routing table entry to the list of entries
            entries.append({
                "destination": destination,
                "gateway": gateway,
                "metric": metric,
                "protocal": protocal,
                "interface": interface
            })
    # Return the list of routing table entries
    return entries

# Call the function to get the FRR routing table information
routing_table = get_frr_routing_table()
# Print the routing table information
print(routing_table)
