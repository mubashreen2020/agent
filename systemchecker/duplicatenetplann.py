import os

def check_duplicate_sections():
    netplan_dir = "/etc/netplan"
    config_files = [f for f in os.listdir(netplan_dir) if os.path.isfile(os.path.join(netplan_dir, f)) and f.endswith(".yaml")]
    
    sections = {}
    for file in config_files:
        with open(os.path.join(netplan_dir, file), "r") as f:
            content = f.read()
            
            for line in content.split("\n"):
                if line.strip().startswith("network:"):
                    section_name = line.strip().split(":")[1].strip()
                    if section_name in sections:
                        return f"Duplicate section '{section_name}' found in {file} and {sections[section_name]}."
                    sections[section_name] = file
    
    return "No duplicate sections found in netplan configuration."

print(check_duplicate_sections())
