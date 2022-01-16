import queue
import threading
import time

serving_line = queue.Queue(maxsize=5)

def cpu_work(work_units):
    x = 0
    for work in range(work_units * 10_000_000):
        x += 1

def soup_producer():
    for i in range(20):
        serving_line.put_nowait(f'Bowl # {i}')
        print('Served Bowl #', str(i), '- remaining capacity:', \
            serving_line.maxsize-serving_line.qsize())
        time.sleep(0.2)
    serving_line.put_nowait("no soup for you")
    serving_line.put_nowait("no soup for you")
        
def soup_consumer():
    while True:
        bowl = serving_line.get()
        if bowl == 'no soup for you':
            break
        print('Ate', bowl)
        cpu_work(4)
        
        
if __name__ == '__main__':
    # an exception occurs as consumers are consuming at a lower rate than producers, try using more threads to resolve 
    # threading.Thread(target=soup_consumer).start()
    # threading.Thread(target=soup_producer).start()
    
    for i in range(5):
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()
    
    """
    Still fails even when the number of threads are increased
    Reason is from the Global interprater Lock (GIL)
    GIL only allows only one thread to execute at a time so creating more threads does not really solve the problem
    To get arround this, we can use multiprocessing package
    
    """