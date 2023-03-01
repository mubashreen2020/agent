import re

def check_hostname_syntax(hostname):
    """
    Check the syntax of a hostname in Linux.
    Returns True if the syntax is valid, False otherwise.
    """
    if len(hostname) > 255:
        return False

    if hostname[-1] == ".":
        hostname = hostname[:-1]

    # Valid hostname regex
    hostname_regex = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$')

    if not hostname_regex.match(hostname):
        return False

    return True
