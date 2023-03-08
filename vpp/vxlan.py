import sys
import socket
from vpp_papi import VPPApi

# Initialize VPPApi instance
vpp_api = VPPApi()

# Get user input
local_address = input("Enter local IP address: ")
remote_address = input("Enter remote IP address: ")
vni = int(input("Enter VNI: "))

# Create tunnel
sw_if_index = vpp_api.create_vxlan_tunnel(local_address, remote_address, vni)

# Enable tunnel
vpp_api.set_interface_state(sw_if_index, True)

print("VXLAN tunnel created with SW_IF_INDEX", sw_if_index)
