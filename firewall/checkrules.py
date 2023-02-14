import subprocess

def firewall_status():
    output = subprocess.run(['iptables', '-L'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if output.returncode == 0:
        print('Firewall is enabled.')
    else:
        print('Firewall is not enabled.')

firewall_status()
