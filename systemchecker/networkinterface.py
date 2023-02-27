import netifaces

# Get a list of all network interfaces
interfaces = netifaces.interfaces()

# Count the number of non-loopback interfaces
num_interfaces = sum(1 for iface in interfaces if iface != 'lo')

# Check if at least 2 non-loopback interfaces are available
if num_interfaces < 2:
    print("Error: At least 2 network interfaces are required.")
else:
    print("Success: Found at least 2 network interfaces.")
