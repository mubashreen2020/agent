import socket

def get_public_ip_of_interface(interface):
    # Get the public IP address of the interface
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    public_ip = s.getsockname()[0]
    s.close()
    
    return public_ip

# Get the public IP address of all interfaces
interfaces = ["eth0", "wlan0", ...]
public_ips = {}
for interface in interfaces:
    public_ips[interface] = get_public_ip_of_interface(interface)
    
print(public_ips)
