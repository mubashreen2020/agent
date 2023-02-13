import subprocess

# Start the VPP service
subprocess.run(["service", "vpp", "start"])

# Check the status of the VPP service
result = subprocess.run(["service", "vpp", "status"], capture_output=True)

# Print the status of the VPP service
print(result.stdout.decode().strip())

