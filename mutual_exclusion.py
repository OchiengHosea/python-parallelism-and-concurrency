import threading
import time

garlic_count = 0
pencil = threading.Lock()

def shopper():
    global garlic_count
    for i in range(5):
        print(threading.current_thread().getName(), 'is thinking')
        time.sleep(0.5)
        pencil.acquire()
        garlic_count += 1
        pencil.release()
        
if __name__ == '__main__':
    shopper1 = threading.Thread(target=shopper)
    shopper2 = threading.Thread(target=shopper)
    
    shopper1.start()
    shopper2.start()
    shopper1.join()
    shopper2.join()
    print('We should buy', garlic_count, 'garlic.')