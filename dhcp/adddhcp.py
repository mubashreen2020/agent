import subprocess

# Configure DHCP
def configure_dhcp(interface, start_ip, end_ip, dns_server):
    # Create the dhcp configuration file
    with open("/etc/dhcpd.conf", "w") as file:
        file.write("subnet 192.168.3.0 netmask 255.255.255.0 {\n")
        file.write("  range 192.168.3.100 192.168.3.150;\n")
        file.write("  option broadcast-address 192.168.3.255;\n")
        file.write("  option routers 192.168.3.1;\n")
        file.write("  default-lease-time 600;\n")
        file.write("  max-lease-time 7200;\n")
        file.write("  option domain-name-servers google.com, google.com;\n")
        file.write("}\n")
    
    # Enable the DHCP service
    subprocess.run(["systemctl", "enable", "dhcpd"])
    subprocess.run(["systemctl", "start", "dhcpd"])
    
    # Restart the network service
    subprocess.run(["systemctl", "restart", "network"])
    
# Call the function
configure_dhcp("eth0", "192.168.3.100", "192.168.3.150", "google.com,google.com")
