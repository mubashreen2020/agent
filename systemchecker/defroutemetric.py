import subprocess

def get_default_route_metric():
    try:
        output = subprocess.check_output(['ip', 'route', 'show', 'default']).decode()
        # Output will be like "default via <ip address> dev <interface> proto dhcp metric <metric value>"
        metric_index = output.find("metric ")  # find the index of "metric" in the output
        metric_value = int(output[metric_index:].split()[1])  # extract the metric value as an integer
        return metric_value
    except subprocess.CalledProcessError:
        # If the command fails to execute, return None or handle the exception as needed
        return None

# Example usage:
default_route_metric = get_default_route_metric()
if default_route_metric is not None:
    print(f"The default route metric is {default_route_metric}.")
else:
    print("Failed to get the default route metric.")
