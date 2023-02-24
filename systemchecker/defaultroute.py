import subprocess

def check_default_route():
    # Run the "ip route" command to get the default route
    output = subprocess.check_output(["ip", "route"])
    lines = output.decode().split('\n')
    default_route = None
    for line in lines:
        if line.startswith("default via "):
            default_route = line.split()[2]
            break

    # Ping a well-known IP address on the Internet
    ping_result = subprocess.call(["ping", "-c", "1", "-W", "1", default_route])

    # Check if the ping was successful
    if ping_result == 0:
        print("Default route has WAN connectivity")
    else:
        print("Default route does not have WAN connectivity")

if __name__ == '__main__':
    check_default_route()
