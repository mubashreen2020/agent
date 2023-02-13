import netifaces

def stop_interface(interface_name):
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
            os.system(f"sudo ifconfig {interface_name} down")
            print(f"{interface_name} stopped successfully")
        else:
            print(f"{interface_name} is already stopped")
    else:
        print(f"{interface_name} not found")

# Call the function to stop the interface
stop_interface("eth0")
