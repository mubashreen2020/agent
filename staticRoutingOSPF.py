import paramiko

# Define the router's IP address and login credentials
router_ip = '192.168.1.1'
username = 'admin'
password = 'password'

# Create a new SSH client and connect to the router
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router_ip, username=username, password=password)

# Identify the network and subnet you want to add a static route to
destination_network = '192.168.1.0'
subnet_mask = '255.255.255.0'

# Determine the IP address of the next hop router
next_hop_router = '10.0.0.1'

# Configure the static route on the router
command = f"ip route {destination_network} {subnet_mask} {next_hop_router}"
stdin, stdout, stderr = ssh.exec_command(command)

# Enable OSPF on the router's interfaces
process_id = '1'
network_address = '10.0.0.0'
wildcard_mask = '0.0.0.255'
area_id = '0'

command = f"router ospf {process_id}\n"
command += f"network {network_address} {wildcard_mask} area {area_id}\n"
stdin, stdout, stderr = ssh.exec_command(command)

# Verify that the static route and OSPF configuration are working
command = "show ip route"
stdin, stdout, stderr = ssh.exec_command(command)
output = stdout.read().decode()
print(output)

# Close the SSH connection
ssh.close()
