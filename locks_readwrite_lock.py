import threading
from readerwriterlock import rwlock

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday"]
today = 0
# marker = threading.Lock()
marker = rwlock.RWLockFair() # give fair access to both write and lock

def calendar_reader(id_number):
    global today
    read_marker = marker.gen_rlock()
    name = 'Reaeder-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        read_marker.acquire()
        print(name, 'sees that today is', WEEKDAYS[today], '-read count:', read_marker.c_rw_lock.v_read_count)
        read_marker.release()
        
def calendar_writer(id_number):
    global today
    write_marker = marker.gen_rlock()
    name = "Writer-" + str(id_number)
    while today < len(WEEKDAYS) -1:
        write_marker.acquire()
        today = (today + 1) % 7
        print(name, 'updated to ', WEEKDAYS[today])
        write_marker.release()
        

if __name__ == '__main__':
    # create ten reader threads
    for i in range(10):
        threading.Thread(target=calendar_reader, args=(i,)).start()
    
    # ... but only 2 writer threads
    for i in range(2):
        threading.Thread(target=calendar_writer, args=(i,)).start()
        