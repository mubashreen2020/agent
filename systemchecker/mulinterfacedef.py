import netifaces

# Get a list of all network interfaces
interfaces = netifaces.interfaces()

# Loop through each interface and print its details
for interface in interfaces:
    details = netifaces.ifaddresses(interface)
    print("Interface:", interface)
    print("Details:", details)
