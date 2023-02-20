import os

# Install dhcpd package
print(os.system(f"sudo apt-get update -y"))
print(os.system(f"sudo apt-get install isc-dhcp-server -y"))

print("enter your lan address")
lan_address = input()
print("enter your netmask")
dhcp_netmask = input()
print("enter your dhcp starting address")
dhcp_start_address = input()
print("enter your dhcp ending address")
dhcp_end_address = input()
print("enter your gateway")
dhcp_gateway = input() 
print("domain name server")
domain_name = input()
print("optional domain name server")
optional_dns = input()
print("enter static ip")
static_ip = input()
bracket = "{"
closebracket ="}"
#Configure dhcpd.conf file
with open("/etc/dhcp/dhcpd.conf", "w") as f:

 f.write(f"default-lease-time 600;\n max-lease-time 7200;\n authoritative;\n subnet {lan_address} netmask {dhcp_netmask} {bracket} \n range {dhcp_start_address} {dhcp_end_address}; \n option routers {dhcp_gateway}; \n option subnet-mask {dhcp_netmask}; \n option domain-name-servers {domain_name}, {optional_dns}; \n {closebracket}")

# Configure network interface
#network_interface = # The primary network interface
with open("/etc/network/interfaces", "w") as w:
 w.write(f"auto enp0s8 \n iface enp0s8 inet static \n \t address {static_ip} netmask {dhcp_netmask} \n \t gateway {dhcp_gateway}")
# Start the dhcpd service
print(os.system(f"sudo systemctl enable isc-dhcp-server"))
print(os.system(f"sudo systemctl start isc-dhcp-server"))
print(os.system(f"sudo systemctl status isc-dhcp-server"))
