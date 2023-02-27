import netifaces

# Get all network interfaces on the system
interfaces = netifaces.interfaces()

# Check if there are at least two network interfaces
if len(interfaces) < 2:
    print("Error: at least two network interfaces are required.")
else:
    print("Success: There are at least two network interfaces.")
