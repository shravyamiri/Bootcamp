import psutil

def print_resources():
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {mem.percent}%")

print_resources()
