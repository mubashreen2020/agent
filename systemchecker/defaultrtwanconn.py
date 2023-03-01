import os

# IP address to ping
ip = '8.8.8.8'

# Ping the IP address and check the result
response = os.system("ping -c 1 " + ip)

if response == 0:
    print("Default route has WAN connectivity.")
else:
    print("Default route does not have WAN connectivity.")
