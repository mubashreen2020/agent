import platform
import subprocess

def has_sse42_support():
    if platform.system() != "Linux":
        # SSE 4.2 support check is only implemented for Linux
        return False

    # Use the cpuid utility to check for SSE 4.2 support
    cpuid_output = subprocess.check_output("cpuid -1", shell=True).decode()
    return "SSE4.2" in cpuid_output

if __name__ == "__main__":
    if has_sse42_support():
        print("SSE 4.2 support is available.")
    else:
        print("SSE 4.2 support is not available.")
