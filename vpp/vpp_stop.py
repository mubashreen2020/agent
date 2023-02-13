import subprocess

def stop_vpp():
    # Stop the VPP service
    subprocess.run(["service", "vpp", "stop"])

    # Check the status of the VPP service
    result = subprocess.run(["service", "vpp", "status"], capture_output=True)

    # Print the status of the VPP service
    print(result.stdout.decode().strip())

# Stop the VPP service
stop_vpp()
