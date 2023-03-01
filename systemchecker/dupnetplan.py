import re

def check_duplicate_sections(file_path):
    """
    Checks for duplicate sections in a Netplan configuration file.
    Returns True if there are duplicates, False otherwise.
    """
    section_names = []
    with open(file_path, 'r') as f:
        content = f.read()
        sections = re.findall(r'^\s*([a-zA-Z0-9_-]+):\s*\n\s*.*?(?=\n[a-zA-Z0-9_-]+:|\Z)', content, re.DOTALL | re.MULTILINE)
        section_names = [s[0] for s in sections]

    return len(section_names) != len(set(section_names))

# Example usage:
if check_duplicate_sections('/etc/netplan/01-netcfg.yaml'):
    print("Duplicate sections found.")
else:
    print("No duplicate sections.")
