import os
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)
    return 10.1