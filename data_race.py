import threading

garlic_count = 0

def shopper():
    global garlic_count
    for i in range(10_000_000):
        garlic_count += 1
        
if __name__ == '__main__':
    shopper1 = threading.Thread(target=shopper)
    shopper2 = threading.Thread(target=shopper)
    
    shopper1.start()
    shopper2.start()
    shopper1.join()
    shopper2.join()
    print('We should buy', garlic_count, 'garlic.')