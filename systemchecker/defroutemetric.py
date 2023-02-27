import subprocess

def get_default_route_metric():
    # Execute the "ip route show" command and capture its output
    ip_route_output = subprocess.check_output(["ip", "route", "show"]).decode()

    # Split the output into lines
    ip_route_lines = ip_route_output.split("\n")

    # Find the line that contains the default route
    default_route_line = None
    for line in ip_route_lines:
        if "default via" in line:
            default_route_line = line
            break

    # Parse the default route line to extract the metric value
    if default_route_line is not None:
        metric_index = default_route_line.find("metric")
        if metric_index != -1:
            metric_str = default_route_line[metric_index:].split()[1]
            return int(metric_str)

    # If no default route was found or it didn't have a metric, return None
    return None

# Example usage:
metric = get_default_route_metric()
if metric is not None:
    print(f"The default route metric is {metric}.")
else:
    print("No default route found.")
