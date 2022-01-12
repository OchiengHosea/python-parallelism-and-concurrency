import threading
import time
from random import random
# causes deadlocks
chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500

def philosopher(name, firstc_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:
        firstc_chopstick.acquire()
        if not second_chopstick.acquire(blocking=False):
            print(name, 'released their first chopstick')
            firstc_chopstick.release()
            time.sleep(random()/10)
        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)
            finally:
                firstc_chopstick.release()
                second_chopstick.release()
        
        
if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Ban', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Nab', chopstick_b, chopstick_c)).start()
    # threading.Thread(target=philosopher, args=('Anb', chopstick_c, chopstick_a)).start()
    # acquire the highest priority lock first
    threading.Thread(target=philosopher, args=('Anb', chopstick_a, chopstick_c)).start()
    
    # Lock ordering and lock timeouts
        