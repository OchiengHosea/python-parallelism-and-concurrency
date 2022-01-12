import threading
WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday"]
today = 0
marker = threading.Lock()

def calendar_reader(id_number):
    global today
    name = 'Reaeder-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        marker.acquire()
        print(name, 'sees that today is', WEEKDAYS[today])
        marker.release()