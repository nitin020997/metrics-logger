import time
import psutil

def get_metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return f"CPU: {cpu}% | Memory: {memory}%"

if __name__ == "__main__":
    while True:
        print(get_metrics())
        time.sleep(5)



print("✅ CPU Usage:", psutil.cpu_percent())
print("✅ Memory Usage:", psutil.virtual_memory().percent)
print("✅ Disk Usage:", psutil.disk_usage('/').percent)