import subprocess

def get_default_route_metric():
    """
    Returns the metric of the default route on Linux systems.
    """
    # Execute the "ip route show" command and capture its output
    output = subprocess.check_output(["ip", "route", "show"]).decode()

    # Split the output into lines and search for the line containing "default via"
    for line in output.split("\n"):
        if "default via" in line:
            # Extract the metric from the line and return it
            metric_index = line.find("metric ") + len("metric ")
            return int(line[metric_index:])

    # If no default route was found, raise an exception
    raise Exception("No default route found")

# Example usage:
try:
    metric = get_default_route_metric()
    print(f"The default route's metric is {metric}")
except Exception as e:
    print(e)
