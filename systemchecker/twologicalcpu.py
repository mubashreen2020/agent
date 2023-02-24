import os

if os.cpu_count() < 2:
    print("Error: This script requires at least 2 logical CPUs.")
else:
    print("Success: This machine has at least 2 logical CPUs.")
