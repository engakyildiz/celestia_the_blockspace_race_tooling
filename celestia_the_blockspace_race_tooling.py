import os
import psutil
import time

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 ** 3) # Convert bytes to GB

def print_node_performance():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    remaining_disk_space = disk_usage.free / (1024 ** 3) # Convert bytes to GB
    celestia_folder = os.path.expanduser('~/.celestia-light-blockspacerace-0/data')
    celestia_folder_size = get_folder_size(celestia_folder)

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%")
    print(f"Disk Usage: {disk_percent}%")
    print(f"Remaining Disk Space: {remaining_disk_space:.2f} GB")
    print(f"Size of .celestia-light-blockspacerace-0/data folder: {celestia_folder_size:.2f} GB")
    print("")

while True:
    print_node_performance()
    time.sleep(5)
