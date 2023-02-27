import subprocess

def check_interfaces(*interfaces):
    for interface in interfaces:
        try:
            subprocess.check_output(["ifconfig", interface])
            print(f"{interface}: Found")
        except subprocess.CalledProcessError:
            print(f"{interface}: Not Found")

# Example usage
check_interfaces("eth0", "lo", "wlan0")
