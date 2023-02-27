import socket

hostname = input("Enter hostname to check: ")

with open('/etc/hosts', 'r') as file:
    for line in file:
        if line.startswith('#'):
            continue
        words = line.split()
        if len(words) < 2:
            continue
        if hostname == words[1]:
            print("Hostname found in hosts file")
            break
    else:
        print("Hostname not found in hosts file")
