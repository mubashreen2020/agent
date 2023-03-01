ximport socket

def is_valid_hostname(hostname):
    """
    Check if a hostname is valid
    """
    try:
        socket.getaddrinfo(hostname, None)
        return True
    except socket.error:
        return False

# Example usage
hostname = "example.com"
if is_valid_hostname(hostname):
    print(f"{hostname} is a valid hostname")
else:
    print(f"{hostname} is not a valid hostname")
