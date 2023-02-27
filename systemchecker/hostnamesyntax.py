import re

def is_valid_hostname(hostname):
    """
    Returns True if the given string is a valid hostname, False otherwise.
    """
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]  # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

# Example usage
hostname = "www.example.com"
if is_valid_hostname(hostname):
    print(f"{hostname} is a valid hostname")
else:
    print(f"{hostname} is not a valid hostname")
