import threading
# causes deadlocks
chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 5000

def philosopher(name, firstc_chopstick, second_chopstick):
    global sushi_count
    sushi_eaten = 0
    while sushi_count > 0:
        with firstc_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                    sushi_eaten += 1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)
                # if sushi_count == 10:
                #     print(1/0)
    print(name, 'took', sushi_eaten, 'pieces')
                    
if __name__ == '__main__':
    for thread in range(50):
        threading.Thread(target=philosopher, args=('Ban', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Nab', chopstick_a, chopstick_b)).start()
        # threading.Thread(target=philosopher, args=('Anb', chopstick_c, chopstick_a)).start()
        # acquire the highest priority lock first
        threading.Thread(target=philosopher, args=('Anb', chopstick_a, chopstick_b)).start()
    
    # Lock ordering and lock timeouts
        