import queue
import threading
import time

serving_line = queue.Queue(maxsize=5)

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
            break;
        print('Ate', bowl)
        time.sleep(0.3)
        
        
if __name__ == '__main__':
    # an exception occurs as consumers are consuming at a lower rate than producers, try using more threads to resolve 
    # threading.Thread(target=soup_consumer).start()
    # threading.Thread(target=soup_producer).start()
    
    for i in range(2):
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()