"""Check how much memory is left"""
from concurrent.futures import ThreadPoolExecutor
import time

def how_much_memory_is_left():
    print("Process is checking memory")
    time.sleep(3)
    return 42
    
if __name__ == '__main__':
    print("User asks how much memory is left")
    with ThreadPoolExecutor() as pool:
        future = pool.submit(how_much_memory_is_left)
        print("User can do other things as they wait")
        print("Process responded with", future.result())