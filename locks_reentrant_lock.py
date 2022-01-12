import threading

garlic_count = 0
potato_count = 0
pencil = threading.RLock()

def add_garlic():
    global garlic_count
    pencil.acquire()
    garlic_count += 1
    pencil.release()
    
def add_potato():
    global potato_count
    pencil.acquire()
    potato_count += 1
    add_garlic()
    pencil.release()

def shopper():
    for i in range(10_000):
        add_garlic()
        add_potato()
        
if __name__ == '__main__':
    shopper1 = threading.Thread(target=shopper)
    shopper2 = threading.Thread(target=shopper)
    
    shopper1.start()
    shopper2.start()
    
    shopper1.join()
    shopper2.join()
    
    print("We should buy ", garlic_count, 'garlic and ', potato_count, ' potatoes')