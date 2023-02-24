import os

def has_sse42_support():
    if os.cpu_count() == 1:
        # If there is only one logical processor, assume SSE 4.2 is supported
        return True
    try:
        import cpuid
    except ImportError:
        # If cpuid module is not available, assume SSE 4.2 is not supported
        return False
    features = cpuid.CPUID().get_feature_info()
    return features.sse4_2

if has_sse42_support():
    print("SSE 4.2 is supported on this CPU.")
else:
    print("SSE 4.2 is not supported on this CPU.")
