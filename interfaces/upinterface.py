import netifaces

def start_interface(interface_name):
    # Get the list of available interfaces
    interfaces = netifaces.interfaces()

    # Check if the specified interface is present
    if interface_name in interfaces:
        # Get the interface's information
        interface_info = netifaces.ifaddresses(interface_name)

        # Check if the interface is running
        if netifaces.AF_INET in interface_info:
            # Use the system's command line interface to stop the interface
            import os
            os.system(f"sudo ifconfig {interface_name} up")
            print(f"{interface_name} started successfully")
        else:
            print(f"{interface_name} is already started")
    else:
        print(f"{interface_name} not found")

# Call the function to stop the interface
start_interface("enp0s3")
