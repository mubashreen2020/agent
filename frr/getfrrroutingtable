import subprocess

def get_routing_table():
    # Use the `vtysh` command to get the routing table
    output = subprocess.run(['vtysh', '-c', 'show ip route'], stdout=subprocess.PIPE).stdout.decode()
    
    # Split the output into lines
    lines = output.splitlines()
    
    # Skip the first line, which is a header
    lines = lines[1:]
    
    # Loop through the lines and extract the information about each route
    routes = []
    for line in lines:
        # Split the line into columns
        columns = line.split()
        
        # Extract the information about the route
        destination = columns[0]
        gateway = columns[1]
        metric = columns[2]
        protocol = columns[3]
        interface = columns[4]
        
        # Add the route information to the list of routes
        routes.append({
            'destination': destination,
            'gateway': gateway,
            'metric': metric,
            'protocol': protocol,
            'interface': interface
        })
    
    # Return the list of routes
    return routes

# Get the information about the routing table
routing_table = get_routing_table()

# Print the information about each route
for route in routing_table:
    print(f'Destination: {route["destination"]}')
    print(f' Gateway: {route["gateway"]}')
    print(f' Metric: {route["metric"]}')
    print(f' Protocol: {route["protocol"]}')
    print(f' Interface: {route["interface"]}')
    print('')
