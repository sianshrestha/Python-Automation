import psutil

def check_server_health():
    print("Server Health Check:")

    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > 80:
        print("Warning: High CPU usage!")

    # Check memory usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    if memory.percent > 80:
        print("Warning: High memory usage!")

    # Check disk usage
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")
    if disk.percent > 80:
        print("Warning: High disk usage!")

    # Check network stats (optional)
    net_io = psutil.net_io_counters()
    print(f"Network: Sent={net_io.bytes_sent} bytes, Received={net_io.bytes_recv} bytes")

if __name__ == "__main__":
    check_server_health()
