import os
import threading
import multiprocessing as mp
"""A simple function that wastes cpu"""
def cpu_waster():
    while True:
        pass

print('Hi! my name is, ', __name__)
if __name__ == '__main__':
    """Display information about this process"""
    print("Process ID: ", os.getpid())
    print('Thread count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)
        
    print("Starting 12 cpu wasters")
    for i in range(32):
        mp.Process(target=cpu_waster).start()
        

    """Display information about this process"""
    print("Process ID: ", os.getpid())
    print('Thread count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)