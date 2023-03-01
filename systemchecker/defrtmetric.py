import subprocess

def get_default_route_metric():
    output = subprocess.check_output(['ip', 'route', 'show'])
    for line in output.decode('utf-8').split('\n'):
        if 'default' in line:
            fields = line.split()
            for i in range(len(fields)):
                if fields[i] == 'metric':
                    return int(fields[i+1])

# Example usage:
default_metric = get_default_route_metric()
print('Default route metric:', default_metric)
