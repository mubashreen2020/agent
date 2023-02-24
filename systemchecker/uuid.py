import subprocess

# Replace /dev/sda1 with the partition you want to check
partition = '/dev/sda1'

# Execute blkid command to get UUID of partition
cmd = ['blkid', '-s', 'UUID', '-o', 'value', partition]
uuid = subprocess.check_output(cmd).decode('utf-8').strip()

# Print UUID of partition
print(f"The UUID of {partition} is {uuid}")
