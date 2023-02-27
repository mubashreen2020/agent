import subprocess

# Execute the "ip route show" command and capture the output
output = subprocess.check_output(['ip', 'route', 'show']).decode()

# Split the output into lines and iterate over them
for line in output.split('\n'):
    # Check if the line contains the default route
    if 'default via' in line:
        # Split the line into fields and extract the metric field
        fields = line.split()
        metric_field = [field for field in fields if 'metric' in field]
        # If a metric field was found, extract the metric value and print it
        if metric_field:
            metric_value = metric_field[0].split()[1]
            print(f"The default route metric is {metric_value}.")
            break
else:
    print("No default route found.")
