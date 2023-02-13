import openvpn_python

# Path to the OpenVPN configuration file
config_file = "/path/to/openvpn.conf"

# Start the OpenVPN connection
vpn = openvpn_python.openvpn_connect(config_file)

# Wait for the connection to be established
while not vpn.is_connected():
    pass

# The VPN connection is now established
print("OpenVPN connection established.")

# Disconnect from the OpenVPN server
vpn.disconnect()
