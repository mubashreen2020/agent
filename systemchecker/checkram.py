import psutil

total_memory = psutil.virtual_memory().total
gb_memory = round(total_memory / (1024 ** 3), 2)

if gb_memory >= 4:
    print(f"System has {gb_memory} GB RAM, which is sufficient.")
else:
    print(f"System has only {gb_memory} GB RAM, which is insufficient.")
