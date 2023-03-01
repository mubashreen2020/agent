import os

def check_wan_connectivity():
    hostname = "www.google.com"
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        print(hostname, 'is up!')
        return True
    else:
        print(hostname, 'is down!')
        return False
