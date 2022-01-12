import threading
import time

def iron_heater():
    while True:
        print('Temperature has been increased')
        time.sleep(1)
        
if __name__ == '__main__':
    second_heater = threading.Thread(target=iron_heater)
    second_heater.daemon = True
    second_heater.start()
    
    print('Second heater is heating...')
    time.sleep(0.6)
    print('Second heater is heating...')
    time.sleep(0.6)
    print('Second heater is heating...')
    time.sleep(0.6)
    print('Heating is done')