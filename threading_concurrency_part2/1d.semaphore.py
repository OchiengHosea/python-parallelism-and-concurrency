"""This is a signalling mechanism for signalling threads
"""

""" Connecting cell phones to a charger"""

import random
import threading
import time

charger = threading.Semaphore(1)

def cellphone():
    name = threading.current_thread().getName()
    with charger:
        print(name, "is charging...")
        time.sleep(random.uniform(1,2))
        print(name, 'is DONE charging!')
    
if __name__ == '__main__':
    for phone in range(10):
        threading.Thread(target=cellphone, name=f"Phone-{phone}").start()
        
# mods
"""
Instead of explicitly acquiring and releasing the charging lock, we can replace 
the action ny using a with context
"""