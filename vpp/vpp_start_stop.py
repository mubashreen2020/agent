import subprocess

def start_vpp():
    # Start the VPP service
    subprocess.run(["service", "vpp", "start"])

    # Check the status of the VPP service
    result = subprocess.run(["service", "vpp", "status"], capture_output=True)

    # Print the status of the VPP service
    print(result.stdout.decode().strip())

def stop_vpp():
    # Stop the VPP service
    subprocess.run(["service", "vpp", "stop"])

    # Check the status of the VPP service
    result = subprocess.run(["service", "vpp", "status"], capture_output=True)

    # Print the status of the VPP service
    print(result.stdout.decode().strip())

# Start the VPP service
start_vpp()

# Stop the VPP service
stop_vpp()
