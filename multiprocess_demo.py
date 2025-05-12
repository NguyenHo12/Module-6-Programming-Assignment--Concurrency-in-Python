### 15.1 – Multiprocessing Note

import multiprocessing
import random
import time
from datetime import datetime

def show_time():
    wait = random.random()
    time.sleep(wait)
    print(f"{multiprocessing.current_process().name} at {datetime.now().strftime('%H:%M:%S')} after {wait:.2f}s")

if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=show_time, name=f"Process-{i+1}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
