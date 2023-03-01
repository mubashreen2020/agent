#!/usr/bin/env python

import os

def check_network_cards():
    # Run the "lspci" command to get the PCI devices information
    output = os.popen('lspci -nn').read()

    # Parse the output to get the network devices
    network_devices = []
    for line in output.splitlines():
        if 'Network controller' in line or 'Ethernet controller' in line:
            network_devices.append(line.strip())

    # Print the network devices
    if network_devices:
        print("Supported Network Cards:")
        for device in network_devices:
            print(device)
    else:
        print("No supported network cards found.")


if __name__ == '__main__':
    check_network_cards()
