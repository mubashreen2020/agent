import subprocess

# Run the "ip route show" command and capture the output
result = subprocess.run(["ip", "route", "show"], capture_output=True, text=True)

# Split the output into lines
lines = result.stdout.split("\n")

# Loop through the lines to find the default route and its metric
for line in lines:
    if line.startswith("default"):
        fields = line.split()
        metric = fields[4]
        print(f"The default route metric is: {metric}")
        break
