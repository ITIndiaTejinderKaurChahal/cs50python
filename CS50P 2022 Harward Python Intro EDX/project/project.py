#Server Resource Utilization Monitoring & Output Report (like CPU, Memory and Disk Utlisation)
#submitted on 04 Sept 2024

import psutil
import sys
import os
"""
    psutil: Used for retrieving and monitoring system resource usage (CPU, memory, disk).
    sys: Used for handling command-line arguments and program termination.
    os: Used for handling file paths and interacting with the file system.
"""

def main():
    """
    Main function to handle command-line arguments and call appropriate functions.
    """
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py [command]")

    command = sys.argv[1].lower()

    if command == 'cpu':
        print(f"CPU Utilization: {get_cpu_utilization()}%")
    elif command == 'memory':
        print(f"Memory Utilization: {get_memory_utilization()}%")
    elif command == 'disk':
        print(f"Disk Utilization: {get_disk_utilization()}%")
    elif command == 'report':
        generate_report()
    else:
        sys.exit("Unknown command. Use 'cpu', 'memory', 'disk', or 'report'.")

def get_cpu_utilization():
    """
    Get the current CPU utilization percentage.

    Returns:
        float: CPU utilization percentage.
    """
    return psutil.cpu_percent(interval=1)

def get_memory_utilization():
    """
    Get the current memory utilization percentage.

    Returns:
        float: Memory utilization percentage.
    """
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_utilization():
    """
    Get the current disk utilization percentage.

    Returns:
        float: Disk utilization percentage.
    """
    disk = psutil.disk_usage('/')
    return disk.percent

def generate_report():
    """
    Generate a report summarizing CPU, memory, and disk utilization.
    """
    cpu = get_cpu_utilization()
    memory = get_memory_utilization()
    disk = get_disk_utilization()

    report = (
        f"Server Resource Utilization Report\n"
        f"---------------------------------\n"
        f"CPU Utilization: {cpu}%\n"
        f"Memory Utilization: {memory}%\n"
        f"Disk Utilization: {disk}%\n"
    )

    with open('resource_report.txt', 'w') as f:
        f.write(report)
    print("Report generated: resource_report.txt")

if __name__ == "__main__":
    main()
