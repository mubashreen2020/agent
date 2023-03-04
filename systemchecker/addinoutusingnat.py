import subprocess

external_interface = 'eth0'
internal_ip = '192.168.1.100'
external_port = '80'
internal_port = '8080'

subprocess.run(['iptables', '-A', 'PREROUTING', '-t', 'nat', '-i', external_interface, '-p', 'tcp', '--dport', external_port, '-j', 'DNAT', '--to-destination', f'{internal_ip}:{internal_port}'])
subprocess.run(['iptables', '-A', 'FORWARD', '-p', 'tcp', '-d', internal_ip, '--dport', internal_port, '-j', 'ACCEPT'])
