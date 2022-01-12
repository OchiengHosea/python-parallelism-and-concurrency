import os
import threading

"""A simple function that wastes cpu"""
def cpu_waster():
    while True:
        pass
    
"""Display information about this process"""
print("Process ID: ", os.getpid())
print('Thread count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)
    
print("Starting 12 cpu wasters")
for i in range(32):
    threading.Thread(target=cpu_waster).start()
    

"""Display information about this process"""
print("Process ID: ", os.getpid())
print('Thread count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)