import os
import sys

def has_sse42_support():
    """
    Check if the CPU supports SSE 4.2 instructions.
    """
    try:
        with open('/proc/cpuinfo') as f:
            for line in f:
                if line.startswith('flags'):
                    flags = line.split(':')[1].strip()
                    return 'sse4_2' in flags.split()
    except IOError:
        pass
    return False

if not has_sse42_support():
    print("SSE 4.2 support is required to run this program.")
    sys.exit(1)

