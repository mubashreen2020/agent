import subprocess

def get_interfaces():
    # Use the `ip` command to get a list of the interfaces
    output = subprocess.run(['ip', 'a'], stdout=subprocess.PIPE).stdout.decode()
    
    # Split the output into lines
    lines = output.splitlines()
    
    # Loop through the lines and extract the information about each interface
    interfaces = []
    current_interface = None
    for line in lines:
        # If the line starts with '3:', it is the start of a new interface
        if line.startswith('3:'):
            # Extract the name of the interface
            name = line.split(':')[1].strip()
            
            # Create a new dictionary to store information about the interface
            current_interface = {'name': name}
            interfaces.append(current_interface)
        else:
            # If the line contains 'inet', it is information about the IP address of the interface
            if 'inet' in line:
                # Extract the IP address
                ip_address = line.split()[1].split('/')[0]
                
                # Store the IP address in the current interface
                current_interface['ip_address'] = ip_address
    
    # Return the list of interfaces
    return interfaces

# Get the information about the interfaces
interfaces = get_interfaces()

# Print the information about each interface
for interface in interfaces:
    print(f'Interface: {interface["name"]}')
    print(f' IP Address: {interface["ip_address"]}')
    print('')
