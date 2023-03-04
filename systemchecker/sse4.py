import os

def check_sse42_support():
    try:
        os.system("grep -q sse4_2 /proc/cpuinfo")
        return True
    except:
        return False

if __name__ == '__main__':
    if check_sse42_support():
        print("SSE 4.2 is supported on this system")
    else:
        print("SSE 4.2 is not supported on this system")
