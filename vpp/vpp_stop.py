import subprocess

def stop_vpp():
    # Stop the VPP service
    subprocess.run(["service", "vpp", "stop"])


# Stop the VPP service
stop_vpp()
