import os

def add_inbound_rule(ip_address):
    os.system("iptables -A INPUT -s {} -j ACCEPT".format(ip_address))

# Example usage
add_inbound_rule("192.168.1.100")
