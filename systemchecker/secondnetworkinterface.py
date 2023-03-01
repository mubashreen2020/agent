import psutil

# Get a list of all network interfaces
net_ifs = psutil.net_if_addrs()

# Count the number of active network interfaces
active_ifs = sum(1 for iface in net_ifs.values() if any(addr.family == 2 for addr in iface))

# Check if there are at least 2 active network interfaces
if active_ifs >= 2:
    print("There are at least 2 network interfaces in this system.")
else:
    print("There are less than 2 network interfaces in this system.")
