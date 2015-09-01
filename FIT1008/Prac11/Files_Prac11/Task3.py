"""
FIT1008 Prac 11 Task 3
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: Creating events for a coffee shop
@created 20141020
@modified 20141020
"""
from Task1 import *
from Task2 import *

def status_gen(pq):
    '''
    @purpose: Generates a status event for each hour from 9-6
    @param: pq - PriorityQueue
    @precondition: A valid priority queue
    @postcondition: 'Status' events are added to the priority queue
    @complexity: O(n) where n is the number of status events
    '''
    #generating status events with hourly increments
    for i in range(10):
        x = 60 + (i * 60)
        pq.add(['Status',x], x)
    return pq


def serving_t3(pq):
    '''
    @purpose: Simulates the coming, serving and going of customers based on Task 3 logic
    @param: pq - a Priority Queue
    @precondition: A valid priority queue with events
    @postcondition: An empty priority queue
    @complexity: O(n) where n is the length of the priority queue
    '''
    #A service queue that uses PriorityQueue class
    svcq = PriorityQueue()

    #initialising variables for keeping track
    hourly_served = 0
    hourly_max = 0
    people = []

    while len(pq) != 0:
        #serve priorityQueue
        event = pq.serve()
        # event[0] index 0 = code, index 1 = cust_id
        if event[0][0] == 'Arrival':

            print('Customer ' + str(event[0][1]) + ' has arrived at ' + convert_time(event[1]))

            #keeping track of number of people at any one time
            hourly_max += 1
            people.append(hourly_max)


            if len(svcq) == 0:
                #if service queue is currently empty, serve now
                serveTime = random.randint(0,5)
                pq.add(['Served', event[0][1]], event[1] + serveTime)

            #basically svcq stores the cust_id and an incremental priority
            svcq.add(event[0][1], svcq.max_priority())

        elif event[0][0] == 'Served':

            if len(svcq) != 0:

                #if service queue got customer, serve-later
                x = svcq.serve()

                if len(svcq) != 0:
                    # if svc queue still has customer, enqueue them
                    x = svcq.peek()[0]
                    serveTime = random.randint(0,5)
                    pq.add(['Served', x], event[1] + serveTime)

                print('Customer ' + str(event[0][1]) + ' has been served at ' + convert_time(event[1]))
                # keeping track of number of people served
                hourly_served += 1

                # each served customer can stay for some time and shoo
                drinkTime = random.randint(0,30)
                pq.add(['Left', event[0][1]], event[1] + drinkTime)

        elif event[0][0] == 'Left':
            #customer leaving
            print('Customer ' + str(event[0][1]) + ' has left the shop at ' + convert_time(event[1]))

            if hourly_max > 0:
                hourly_max -= 1

        elif event[0][0] == 'Status':
            # hourly status check
            print('>> Status Check: ' + convert_time(event[1]))
            print('>> Served in last hour: ' + str(hourly_served))
            try:
                print('>> Max in shop: ' + str(max(people)))
            except:
                print('>> Max in shop: 0')

            #reinitialise
            hourly_served = 0
            hourly_max = 0
            people = []

    return pq

#test functions
def test_status_gen():
    print("\nTesting generating status events from 9am-6pm (60-600)")
    pq = PriorityQueue()
    pq = status_gen(pq)
    pq.print_all()

def test_serving_t3():
    pq = PriorityQueue()
    pq = status_gen(pq)
    pq = create_arrival(pq, 200)
    print("\nTesting serving_t3() with randomly generated arrival events")
    serving_t3(pq)


if __name__ == "__main__":
    test_status_gen()
    test_serving_t3()