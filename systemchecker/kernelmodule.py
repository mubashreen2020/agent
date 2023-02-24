import os

# Check if the "kernelhas" directory exists in the "/sys/class/" directory
if os.path.exists("/sys/class/kernelhas"):
    # Read the "version" file in the "kernelhas" directory to get the version information
    with open("/sys/class/kernelhas/version", "r") as f:
        version = f.readline().strip()
        print("Kernelhas version: {}".format(version))

    # Read the "io" file in the "kernelhas" directory to get I/O module information
    with open("/sys/class/kernelhas/io", "r") as f:
        io_modules = f.readline().strip().split(",")
        print("Kernelhas I/O modules: {}".format(io_modules))

else:
    print("Kernelhas not installed.")
