
import subprocess

# Start the OpenVPN service
subprocess.run(["service", "openvpn", "start", "server"])

