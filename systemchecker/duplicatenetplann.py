import os

def check_duplicate_netplan_sections():
    """
    This function checks for duplicate netplan sections in /etc/netplan directory.
    """
    netplan_files = os.listdir('/etc/netplan')
    section_names = []
    for filename in netplan_files:
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open('/etc/netplan/' + filename) as file:
                lines = file.readlines()
                for line in lines:
                    if 'network:' in line:
                        section_name = line.split(':')[1].strip()
                        if section_name in section_names:
                            print(f"Duplicate section found in {filename}: {section_name}")
                        else:
                            section_names.append(section_name)

if __name__ == '__main__':
    check_duplicate_netplan_sections()
