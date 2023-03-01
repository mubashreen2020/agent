import subprocess

def check_default_route():
    output = subprocess.check_output(["ip", "route", "show"]).decode("utf-8")
    for line in output.splitlines():
        if "default via" in line:
            return line.split()[2]

default_route = check_default_route()
if default_route:
    print("Default route:", default_route)
else:
    print("No default route found.")
