import subprocess

def get_interface_names():
    cmd = "ifconfig -a | grep -o '^[^ ]\+'"
    output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
    return output.splitlines()

if __name__ == "__main__":
    interface_names = get_interface_names()
    print("Interface names:")
    print(interface_names)
