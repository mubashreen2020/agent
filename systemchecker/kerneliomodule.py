import os

# Check if the /proc/modules file exists
if not os.path.exists('/proc/modules'):
    print('Error: /proc/modules file not found')
else:
    # Open the /proc/modules file and read its contents
    with open('/proc/modules', 'r') as f:
        modules = f.readlines()

    # Loop through the modules and check if any I/O modules are loaded
    io_modules = ['ata_piix', 'ahci', 'nvme', 'nvme-core', 'nvme-ns']
    io_loaded = False
    for module in modules:
        name = module.split()[0]
        if name in io_modules:
            io_loaded = True
            print(f'{name} module is loaded')
    
    # If no I/O modules are loaded, print a message
    if not io_loaded:
        print('No I/O modules are loaded')
