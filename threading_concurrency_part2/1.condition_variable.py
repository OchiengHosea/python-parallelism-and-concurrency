import threading
"""two hungry persons, anxiosly waiting for their turn to take soup"""
slowcooker_lid = threading.Lock()
soup_servings = 11
# problem
def hungry_person(person_id):
    global soup_servings
    while soup_servings > 0:
        with slowcooker_lid:
            if (person_id == (soup_servings % 2)) and (soup_servings > 0):
                soup_servings -= 1
                print("Person", person_id, 'took soup! Servings left:', soup_servings)
            else:
                print('Person', person_id, 'checked... then put the lid back')
                
# if __name__ == '__main__':
#     for person in range(2):
#         threading.Thread(target=hungry_person, args=(person,)).start()
        
        
# solution 
"""The basic idea is to make threads wait for execution untill they are signalled by another condition"""

slowcooker_lid = threading.Lock()
soup_servings = 11
soup_taken = threading.Condition(lock=slowcooker_lid)
def hungry_person_conditional(person_id):
    global soup_servings
    while soup_servings > 0:
        with slowcooker_lid:
            while (person_id != (soup_servings % 5)) and (soup_servings > 0):
                print('Person', person_id, 'checked... then put the lid back')
                soup_taken.wait()
            if(soup_servings > 0):
                soup_servings -= 1 # turn take
                print("Person", person_id, 'took soup! Servings left:', soup_servings)
                soup_taken.notifyAll()
                
if __name__ == '__main__':
    for person in range(5):
        threading.Thread(target=hungry_person_conditional, args=(person,)).start()
        