import threading
import time

striking = True

def nail_striker():
    name = threading.current_thread().getName();
    stroke_count = 0
    while striking:
        print(name, 'Stoke a nail')
        stroke_count += 1
    print(name, 'stroke', stroke_count, 'strikes.')
    
if __name__ == '__main__':
    threading.Thread(target=nail_striker, name='Hammer A').start()
    threading.Thread(target=nail_striker, name='Hammer B').start()
    
    time.sleep(1)
    striking = False
        