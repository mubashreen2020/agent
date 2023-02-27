import os

def check_io_modules():
    output = os.popen('lsmod').read()
    if 'i915' in output and 'i2c_i801' in output:
        print('The kernel has I/O modules.')
    else:
        print('The kernel does not have I/O modules.')

if __name__ == '__main__':
    check_io_modules()
