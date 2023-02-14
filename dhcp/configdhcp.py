import subprocess

def configure_dhcp(ip_range_start, ip_range_end, dns_server):
    # Define the IP range
    ip_range = f"subnet 192.168.3.0 netmask 255.255.255.0 {\n\trange {ip_range_start} {ip_range_end};\n}"

    # Specify the DNS server
    dns = f"\toption domain-name-servers {dns_server};\n}"

    # Write the configuration to the file
    with open("/etc/dhcp/dhcpd.conf", "w") as f:
        f.write(ip_range + dns)

    # Start the DHCP server
    subprocess.call(["service", "isc-dhcp-server", "start"])

# Example usage
configure_dhcp("192.168.3.100", "192.168.3.200", "8.8.8.8")
