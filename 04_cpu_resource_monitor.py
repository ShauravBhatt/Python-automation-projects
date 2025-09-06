"""
 Challenge: Real-Time System Resource Monitor

Goal:
- Monitor your system's CPU, RAM, and Disk usage
- Print updates every few seconds
- Warn user if CPU or RAM usage exceeds 80%
- Runs in terminal as a live dashboard

Teaches: psutil, formatting, real-time monitoring, conditional logic
Tools: psutil, time
"""

import os 
import psutil
import time 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_stats():
    print("-------- System Resource Monitor --------\n");
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("CPU USAGE: ",cpu)
    print(f"RAM USAGE: {ram.percent}% | {round(ram.used/1e9 , 2)} GB out of {round(ram.total/1e9,2)} GB ")
    print(f"DISK USAGE: {disk.percent}% | {round(disk.used/1e9 , 2)} GB out of {round(disk.total/1e9,2)} GB ")


    print("\nThanks for using !!")

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            show_stats()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n Resource Monitor Stopped !!")
