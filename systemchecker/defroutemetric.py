import subprocess

# Execute the ip route command
output = subprocess.check_output(["ip", "route"])

# Parse the output to find the default route metric
for line in output.decode().splitlines():
    if "default via" in line:
        fields = line.split()
        metric_index = fields.index("metric") + 1
        default_metric = int(fields[metric_index])
        break

print("Default route metric:", default_metric)
