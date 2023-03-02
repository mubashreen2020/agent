import subprocess

# Execute "ip route show" command and capture its output
output = subprocess.check_output(['ip', 'route', 'show']).decode()

# Split the output into lines and iterate over them
for line in output.splitlines():
    # Check if the line contains the default route
    if 'default via' in line:
        # Split the line into tokens and retrieve the metric
        tokens = line.split()
        metric = int(tokens[tokens.index('metric') + 1])
        print(f"Default route metric is {metric}")
        break
else:
    print("Default route not found")
