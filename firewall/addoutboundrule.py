import subprocess

def add_outbound_rule(protocol, destination, port, action):
    # Define the iptables command
    iptables_cmd = f"iptables -A OUTPUT -p {protocol} -d {destination} --dport {port} -j {action}"

    # Execute the iptables command
    subprocess.run(iptables_cmd, shell=True, check=True)

# Example usage:
add_outbound_rule("tcp", "8.8.8.8", "80", "ACCEPT")
