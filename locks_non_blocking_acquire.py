import threading
import time

items_on_notepad = 0
pencil = threading.Lock()

def shopper():
    global items_on_notepad
    name = threading.current_thread().getName()
    items_to_add = 0
    while items_on_notepad <= 20 and pencil.acquire(blocking=False):
        if items_to_add:
            items_on_notepad += items_to_add
            print(name, 'added', items_to_add, 'item(s) to notepad.')
            items_to_add = 0
            time.sleep(0.3)
            pencil.release()
        else:
            time.sleep(0.1)
            items_to_add += 1
            print(name, 'found_something else to buy.')
                        
if __name__ == '__main__':
    shopper1 = threading.Thread(target=shopper, name='shopper2')
    shopper2 = threading.Thread(target=shopper, name='shopper1')
    start_time = time.perf_counter()
    
    shopper1.start()
    shopper2.start()
    
    shopper1.join()
    shopper2.join()
    elapsed_time = time.perf_counter() - start_time
    print('Elapsed Time: {:.2f} seconds'.format(elapsed_time))