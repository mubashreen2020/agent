import subprocess

def disconnect_openvpn():
    try:
        # Use subprocess to run the "pkill" command to kill the OpenVPN process
        subprocess.call("pkill openvpn", shell=True)
        print("OpenVPN has been disconnected.")
    except subprocess.CalledProcessError as e:
        print("Error: Failed to disconnect OpenVPN. Error code: {}".format(e.returncode))

disconnect_openvpn()
