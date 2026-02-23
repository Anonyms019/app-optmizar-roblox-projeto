import psutil

def monitor_performance():
    print("Monitorando uso de CPU e RAM...")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    print(f"CPU: {cpu}% | RAM: {ram}%")
