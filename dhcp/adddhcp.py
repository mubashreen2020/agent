import os

# Install dhcpd package
os.system("sudo apt-get update")
os.system("sudo apt-get install isc-dhcp-server")

# Configure dhcpd.conf file
dhcpd_conf = """default-lease-time 600;
max-lease-time 7200;
subnet 192.168.1.0 netmask 255.255.255.0 {
range 192.168.1.10 192.168.1.100;
option routers 192.168.1.1;
option domain-name-servers 8.8.8.8, 8.8.4.4;
}"""
with open("/etc/dhcp/dhcpd.conf", "w") as f:
    f.write(dhcpd_conf)

# Configure network interface
network_interface = """# The primary network interface
auto eth0
iface eth0 inet static
    address 192.168.1.1
    netmask 255.255.255.0
    gateway 192.168.1.1"""
with open("/etc/network/interfaces", "a") as f:
    f.write(network_interface)

# Start the dhcpd service
os.system("sudo systemctl enable isc-dhcp-server")
os.system("sudo systemctl start isc-dhcp-server")
