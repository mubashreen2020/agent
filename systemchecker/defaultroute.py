import subprocess

def check_default_route():
    output = subprocess.check_output(['ip', 'route', 'show']).decode()
    for line in output.split('\n'):
        if 'default via' in line:
            return True
    return False

if __name__ == '__main__':
    if check_default_route():
        print('Default route exists.')
    else:
        print('No default route found.')
