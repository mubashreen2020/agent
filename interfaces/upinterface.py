import subprocess

def start_interface(interface_name):
    subprocess.run(["ip", "link", "set", interface_name, "up"])

start_interface("enp0s3")
