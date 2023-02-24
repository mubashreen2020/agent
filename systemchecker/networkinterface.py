import psutil

def check_network_interfaces():
    """
    Check if there are at least 2 network interfaces available on the system.
    """
    count = 0
    for interface, addrs in psutil.net_if_addrs().items():
        if interface != "lo":
            count += 1
        if count >= 2:
            return True
    return False

if __name__ == "__main__":
    if check_network_interfaces():
        print("There are at least 2 network interfaces available on the system.")
    else:
        print("There are not enough network interfaces available on the system.")
