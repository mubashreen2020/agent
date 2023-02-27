import netifaces

interfaces = netifaces.interfaces()

if len(interfaces) < 2:
    print("At least 2 network interfaces are required.")
else:
    print("There are at least 2 network interfaces.")

