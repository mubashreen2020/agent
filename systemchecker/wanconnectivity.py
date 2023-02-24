import subprocess

def check_wan_connectivity():
    try:
        # Ping Google DNS server (8.8.8.8) 3 times, and wait no more than 2 seconds for a response.
        subprocess.check_output(['ping', '-c', '3', '-w', '2', '8.8.8.8'])
        return True
    except subprocess.CalledProcessError:
        return False

if check_wan_connectivity():
    print("WAN connectivity is available.")
else:
    print("WAN connectivity is not available.")
