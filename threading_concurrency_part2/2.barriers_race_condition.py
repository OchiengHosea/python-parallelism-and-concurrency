"""Deciding how many bags of chips to buy for the party"""
import threading

bags_of_chips = 1
pencil = threading.Lock()

def cpu_work(work_units):
    x = 0
    for work in range(work_units*1_000_000):
        x += 1
        
def shopper():
    global bags_of_chips
    cpu_work(1)
    with pencil:
        bags_of_chips *= 2
        print('Shopper doubled the bags of chips')
        
def shopper2():
    global bags_of_chips
    cpu_work(1)
    with pencil:
        bags_of_chips += 3
        print('Shopper 2 added 3 bags of chips')
        
if __name__ == '__main__':
    shoppers = []
    for s in range(5):
        shoppers.append(threading.Thread(target=shopper))
        shoppers.append(threading.Thread(target=shopper2))
        
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print('We need to buy', bags_of_chips, 'bags of chips.')
    

# the prorgam suffers from race condition due to the order of execution, this can
# be corrected using a barrier
# A barrier prevents a group of threads from proceeding until enough threads have reached
# the barrier