import json

def get_machine_id():
    with open('/etc/machine-id', 'r') as f:
        return {'machine_id': f.read().strip()}

machine_id_json = json.dumps(get_machine_id())
print(machine_id_json)
