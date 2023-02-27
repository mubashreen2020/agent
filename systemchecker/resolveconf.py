import os

def check_resolvconf():
    if os.path.exists('/etc/resolvconf/resolv.conf.d'):
        print('resolvconf is installed.')
    else:
        print('resolvconf is not installed.')

if __name__ == '__main__':
    check_resolvconf()
