import subprocess

# Define the DHCP configuration file path
dhcp_conf_file = '/etc/dhcp/dhcpd.conf'

# Define the DHCP service name
dhcp_service_name = 'isc-dhcp-server'

# Define the DHCP interface name
dhcp_interface = 'enp0s8'

# Define the DHCP IP range start
dhcp_ip_range_start = '192.168.3.100'

# Define the DHCP IP range end
dhcp_ip_range_end = '192.168.3.200'

# Define the DHCP DNS server
dhcp_dns_server = '8.8.8.8'

# Define the DHCP configuration
dhcp_config = '''
subnet 192.168.3.0 netmask 255.255.255.0 {
  range {}; {}
  option broadcast-address 192.168.3.255;
  option routers 192.168.3.1;
  option domain-name-servers {};
}
'''.format(dhcp_ip_range_start, dhcp_ip_range_end, dhcp_dns_server)

# Write the DHCP configuration to the file
with open(dhcp_conf_file, 'w') as f:
    f.write(dhcp_config)

# Restart the DHCP service
subprocess.call(['sudo', 'systemctl', 'restart', dhcp_service_name])

# Enable the DHCP service
subprocess.call(['sudo', 'systemctl', 'enable', dhcp_service_name])

# Add the DHCP interface
subprocess.call(['sudo', 'ifconfig', dhcp_interface, 'up'])
