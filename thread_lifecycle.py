import threading
import time

class SmithA(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        print('Smith A started and waiting for iron to melt...')
        time.sleep(3)
        print('Smith A is done striking the iron.')
        

if __name__ == '__main__':
    print("Smith B started and requesting Smith A  help")
    smithA = SmithA()
    print(' Smith A alive? ', smithA.is_alive())
    
    print("Smith B tells Smith A to start")
    smithA.start()
    print(' Smith A alive? ', smithA.is_alive())
    
    print('Smith A continues striking iron')
    time.sleep(0.5)
    print(' Smith B alive? ', smithA.is_alive())
    
    print('Smith A patiently waits for Smith B to finish to striking')
    smithA.join()
    print(' Smith A alive? ', smithA.is_alive())
    
    print('Smith A and Smith B are both done!')