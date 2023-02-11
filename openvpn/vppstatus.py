import subprocess

def is_vpp_running():
    try:
        # Use subprocess to run the "pgrep" command
        output = subprocess.check_output("pgrep vpp", shell=True)
        # If VPP is running, the output of the command will not be empty
        if output:
            return True
    except subprocess.CalledProcessError:
        # If VPP is not running, the "pgrep" command will return a non-zero exit code
        pass

    return False

if is_vpp_running():
    print("VPP is running")
else:
    print("VPP is not running")
