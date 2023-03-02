import psutil

# Get total RAM in bytes
total_ram = psutil.virtual_memory().total

# Convert bytes to GB
gb_ram = total_ram / (1024 * 1024 * 1024)

# Check if RAM is at least 4GB
if gb_ram >= 4:
    print("System has at least 4GB of RAM.")
else:
    print("System has less than 4GB of RAM.")
