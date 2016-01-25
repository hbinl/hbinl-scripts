"""
FIT1008 Prac 11 Task Advanced
Loh Hao Bin 25461257
@purpose: Object Oriented?
@created 20141021
@modified 20141021
"""
import random
from Task1 import PriorityQueue
from Task2 import convert_time

class Store:
    def __init__(self):
        self.current_customer = 0
        self.hourly_served = 0
        self.hourly_max = 0
        self.people = []

        self.pq = PriorityQueue()       # Store event queue
        self.svcq = PriorityQueue()     # Store service queue
        self.seats = 50
        self.seated = 0

    def create_events(self, n):
        '''
        @purpose: Creates status & customer arrival events and insert them into the store queue
        @param: pq - Priority Queue, n - number to create
        @precondition: Priority queue initialised
        @postcondition: n arrival events created
        @complexity: O(n) where n is the number of arrival events to create
        '''
        try:
            for i in range(10):
                x = 60 + (i * 60)
                self.pq.add( Status(x), x )
            for i in range(int(n)):
                x = random.randint(0,600)
                self.pq.add( Arrival(x, i), x )
        except ValueError:
            print("Invalid _number to create_ parameter.")

    def queue(self):
        '''
        @purpose: Priority Queue Getter
        @param: None
        @precondition: Priority queue initialised
        @postcondition: returns the priority queue
        @complexity: O(1)
        '''
        return self.pq

    def setQueue(self, pq):
        '''
        @purpose: Priority Queue Setter
        @param: pq - Priority Queue to replace
        @precondition: Priority queue initialised
        @postcondition: Priority queue replaced
        @complexity: O(1)
        '''
        self.pq = pq

    def serviceq(self):
        '''
        @purpose: Service Queue Getter
        @param: None
        @precondition: Priority queue initialised
        @postcondition: returns the service queue
        @complexity: O(1)
        '''
        return self.svcq

    def setServiceq(self, pq):
        '''
        @purpose: Service Queue Setter
        @param: pq - Priority Queue to replace
        @precondition: Priority queue initialised
        @postcondition: Service queue replaced
        @complexity: O(1)
        '''
        self.svcq = pq

class Event:
    def __init__(self, time):
        self.time = time

    def __lt__(self, b):
        '''
        @purpose: Less than
        @param: b - the comparison
        @precondition: Event initialised
        @postcondition: Returns whether self.time < b.time
        @complexity: O(1)
        '''
        if self.time < b.time:
            return True
        else:
            return False

    def __gt__(self, b):
        '''
        @purpose: Greater than
        @param: b - the comparison
        @precondition: Event initialised
        @postcondition: Returns whether self.time > b.time
        @complexity: O(1)
        '''
        if self.time > b.time:
            return True
        else:
            return False

    def __le__(self, b):
        '''
        @purpose: Less than or equal to
        @param: b - the comparison
        @precondition: Event initialised
        @postcondition: Returns whether self.time <= b.time
        @complexity: O(1)
        '''
        if self.time <= b.time:
            return True
        else:
            return False

    def __ge__(self, b):
        '''
        @purpose: Greater than or equal to
        @param: b - the comparison
        @precondition: Event initialised
        @postcondition: Returns whether self.time >= b.time
        @complexity: O(1)
        '''
        if self.time >= b.time:
            return True
        else:
            return False

    def process(self, store, pq):
        pass

class Arrival(Event):
    def __init__(self, time, id):
        Event.__init__(self, time)
        self.id = id                #customer id

    def process(self, store, pq):
        '''
        @purpose: Process for Arrival Event
        @param: store - the store object, pq - the store priority queue
        @precondition: Store and Event initialised
        @postcondition: Arrival event processed
        @complexity: O(log n) where n is the number of items in the queue
        '''
        print('Customer ' + str(self.id) + ' has arrived at ' + convert_time(self.time))
        store.hourly_max += 1
        store.people.append(store.hourly_max)

        if len(store.serviceq()) == 0:
            #if service queue is currently empty, serve now
            serveTime = random.randint(0,5) + self.time
            obj = Served(serveTime, self.id)
            pq.add( obj , serveTime )
            store.setQueue(pq)

        #basically svcq stores the cust_id and an incremental priority
        store.serviceq().add(self.id, store.serviceq().max_priority())
        store.setServiceq(store.serviceq())


class Served(Event):
    def __init__(self, time, id):
        Event.__init__(self, time)
        self.id = id

    def process(self, store, pq):
        '''
        @purpose: Process for Served Event
        @param: store - the store object, pq - the store priority queue
        @precondition: Store and Event initialised
        @postcondition: Served event processed
        @complexity: O(log n) where n is the number of items in the queue
        '''
        if len(store.serviceq()) != 0:
            store.hourly_served += 1

            store.serviceq().serve()
            print('Customer ' + str(self.id) + ' has been served at ' + convert_time(self.time))
            drinkTime = random.randint(0,30) + self.time
            pq.add( Leaving(drinkTime, self.id), drinkTime)
            store.setQueue(pq)

            if len(store.serviceq()) != 0:
                x = store.serviceq().peek()[0]
                serveTime = random.randint(0,5) + self.time
                pq.add( Served(serveTime, x), serveTime)
                store.setQueue(pq)

class Leaving(Event):
    def __init__(self, time, id):
        Event.__init__(self, time)
        self.id = id

    def process(self, store, pq):
        '''
        @purpose: Process for Leaving Event
        @param: store - the store object, pq - the store priority queue
        @precondition: Store and Event initialised
        @postcondition: Leaving event processed
        @complexity: O(1)
        '''
        print('Customer ' + str(self.id) + ' has left the shop at ' + convert_time(self.time))

        if store.hourly_max > 0:
            store.hourly_max -= 1

class Status(Event):
    def __init__(self, time):
        Event.__init__(self, time)

    def process(self, store, pq):
        '''
        @purpose: Process for Status Event
        @param: store - the store object, pq - the store priority queue
        @precondition: Store and Event initialised
        @postcondition: Status event processed
        @complexity: O(1)
        '''
        print('>> Status Check: ' + convert_time(self.time))
        print('>> Served in last hour: ' + str(store.hourly_served))
        try:
            print('>> Max in shop: ' + str(max(store.people)))
        except:
            print('>> Max in shop: 0')

            #reinitialise
        store.hourly_served = 0
        store.hourly_max = 0
        store.people = []


def test_adv_main():
    print("HUEHUEHUEHUE CAFE")
    s = Store()
    s.create_events(200)
    while len(s.queue()) != 0:
        e = (s.queue().serve())
        e[0].process(s, s.queue())




if __name__ == "__main__":
    test_adv_main()
