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