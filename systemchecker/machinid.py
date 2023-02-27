def get_machine_id():
    with open('/etc/machine-id', 'r') as f:
        return f.read().strip()

machine_id = get_machine_id()
print(f'Machine ID: {machine_id}')