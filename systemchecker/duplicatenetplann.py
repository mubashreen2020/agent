import os

def check_duplicate_netplan_sections():
    netplan_dir = '/etc/netplan/'
    netplan_files = os.listdir(netplan_dir)

    for filename in netplan_files:
        if filename.endswith('.yaml'):
            file_path = os.path.join(netplan_dir, filename)
            with open(file_path, 'r') as f:
                sections = {}
                section_name = None
                line_number = 0
                for line in f:
                    line_number += 1
                    stripped_line = line.strip()
                    if stripped_line.startswith('network:'):
                        section_name = stripped_line.split(':')[1].strip()
                        if section_name in sections:
                            print(f'Duplicate netplan section "{section_name}" found in file "{filename}" at line {line_number}.')
                        else:
                            sections[section_name] = True

if __name__ == '__main__':
    check_duplicate_netplan_sections()
