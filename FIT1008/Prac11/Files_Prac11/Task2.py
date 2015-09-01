"""
FIT1008 Prac 11 Task 2
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: Creating events for a coffee shop
@created 20141020
@modified 20141020
"""

import Task1
import random


def create_arrival(pq, n):
    '''
    @purpose: Creates 200 customer arrival events and insert them into the queue
    @param: pq - Priority Queue, n - number to create
    @precondition: Priority queue initialised
    @postcondition: 200 arrival events created
    @complexity: O(n) where n is the number of arrival events to create
    '''
    try:
        for i in range(int(n)):
            # i is for customer ID
            pq.add(['Arrival',i], random.randint(0,600))
        return pq
    except ValueError:
        print("Invalid _number to create_ parameter.")
        return pq

def convert_time(n):
    '''
    @purpose: Converts
    @param: n - The number to be converted to time
    @precondition: none
    @postcondition: returns the time a customer arrives or is served or leaves
    @complexity: O(1)
    '''
    try:
        n = int(n)
        if n >= 0:
            minutes = n % 60
            hour = int( (n - minutes) / 60 + 8 )
            minutes = str(minutes).zfill(2)
            return str(hour) + ':' + minutes
        else:
            raise ValueError
    except ValueError:
        return 'Error. N is invalid.'

def serving(pq):
    '''
    @purpose: notes when a customer arrives, is served and leaves
    @param: none
    @precondition: a valid priority queue
    @postcondition: an empty priority queue
    @complexity: O(n) where n is the length of the priorityqueue
    '''
    while len(pq) != 0:
        event = pq.serve()
        if event[0] == 'Arrival':
            print('Customer has arrived at ' + convert_time(event[1]))
            serveTime = random.randint(0,5)
            pq.add('Served', event[1] + serveTime)
        elif event[0] == 'Served':
            print('Customer has been served at ' + convert_time(event[1]))
            drinkTime = random.randint(0,30)
            pq.add('Left', event[1] + drinkTime)
        elif event[0] == 'Left':
            print('Customer has left the shop at ' + convert_time(event[1]))
    return pq

#Test functions
def test_create_arrival():
    pq = Task1.PriorityQueue()
    print('Testing to create 200 arrival events.')
    pq = create_arrival(pq, 200)
    pq.print_all()
    print('Test success.')
    #for i in range(len(pq)):
    #    print(pq.serve())
    print()

def test_convert_time():
    print('Valid input: Testing to find 75 minutes past 8am')
    print(convert_time(75))
    print(convert_time(605))
    print(convert_time(125))
    print(convert_time(155))
    print(convert_time(452))
    print('\nInvalid input: Testing to find - _ minutes past 8am')
    print(convert_time('_'))
    print('\nInvalid input: Testing to find -60 minutes before 8am')
    print(convert_time(-60))
    print('Test success.')
    print()

def test_serving():
    pq = Task1.PriorityQueue()
    #pq = create_arrival(pq)
    pq.reset()
    print('Testing to find the time when the customer is served and leaves if the customer arrives at 5.00pm.')
    pq.add('Arrival', 540)
    pq = serving(pq)
    #print('Test success.')
    pq.reset()
    print('\nTesting to find the time when the customer is served and leaves if the customer arrives at 12.00pm.')
    pq.add('Arrival', 240)
    pq = serving(pq)
    #print('Test success.')
    pq.reset()
    print('\nTesting to find the time when the customer is served and leaves if the customer arrives at 9.39am.')
    pq.add('Arrival', 99)
    pq = serving(pq)
    #print('Test success.')


def t2_menu():
    test_create_arrival()
    test_convert_time()
    test_serving()

if __name__ == "__main__":
    t2_menu()
