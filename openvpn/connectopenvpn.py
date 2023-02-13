
import subprocess

# Start the OpenVPN service
subprocess.run(["service", "openvpn", "start", "server"])
        print("OpenVPN has connected Successfully.")
    except subprocess.CalledProcessError as e:
        print("Error: Failed to disconnect OpenVPN. Error code: {}".format(e.returncode))

