import yaml

def check_duplicate_netplan_sections():
    with open('/etc/netplan/*.yaml', 'r') as f:
        data = yaml.safe_load_all(f)
        sections = {}
        for doc in data:
            if 'network' in doc:
                if doc['network'] in sections:
                    print(f"Error: Duplicate netplan section found: {doc['network']}")
                else:
                    sections[doc['network']] = True

check_duplicate_netplan_sections()
