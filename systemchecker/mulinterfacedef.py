import subprocess

def get_interfaces():
    output = subprocess.check_output(['ip', 'addr'])
    output = output.decode('utf-8')
    lines = output.split('\n')
    interfaces = []
    current_interface = None
    for line in lines:
        line = line.strip()
        if line.startswith('inet '):
            if current_interface is not None:
                interfaces.append(current_interface)
            current_interface = {'ip_address': line.split()[1]}
        elif line.startswith('inet6 '):
            current_interface['ipv6_address'] = line.split()[1]
        elif line.startswith('link/'):
            current_interface['mac_address'] = line.split()[1]
            current_interface['interface_name'] = line.split()[-1].strip(':')
    if current_interface is not None:
        interfaces.append(current_interface)
    return interfaces

interfaces = get_interfaces()
for interface in interfaces:
    print('Interface:', interface['interface_name'])
    print('  IP address:', interface.get('ip_address', 'N/A'))
    print('  IPv6 address:', interface.get('ipv6_address', 'N/A'))
    print('  MAC address:', interface.get('mac_address', 'N/A'))
