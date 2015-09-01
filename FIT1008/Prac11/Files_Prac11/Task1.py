"""
FIT1008 Prac 11 Task 1
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose:
@created 20141019
@modified 20141019
"""

class PriorityQueue:
    def __init__(self):
        # initialises a priority queue
        self.count = 0
        self.array = [None]

    def __len__(self):
        '''
        @purpose: Returns the number of items in the queue
        @param: None
        @complexity: O(1)
        @precondition: PriorityQueue initialised
        @postcondition: Returns count
        '''
        return self.count

    def add(self, item, priority):
        '''
        @purpose: Add an item in the queue
        @param: Item: The item to be added
                Priority: The priority
        @complexity:
            Best Case: O(1)
            Worst Case: O(log n) where n is the number of items
        @precondition: PriorityQueue initialised
        @postcondition: Returns count
        '''
        try:
            priority = int(priority)
            if self.count + 1 < len(self.array):
                self.array[self.count+1] = [item, priority]
            else:
                self.array.append([item, priority])

            self.count += 1
            self.rise(self.count)
        except ValueError:
            raise TypeError("Non int priority")


    def swap(self, x, y):
        '''
        @purpose: Swaps two items
        @param: x & y: the items to be swapped
        @complexity: O(1)
        @precondition: PriorityQueue initialised
        @postcondition: x and y swapped position
        '''
        tmp = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = tmp

    def rise(self, k):
        '''
        @purpose: Maintains the heap order by rising the item
        @param: k - index of the item to rise
        @complexity:
            O(1) best
            O(log n) where n is the number of items
        @precondition: PriorityQueue initialised
        @postcondition: The item is placed at position fulfilling heap order
        '''
        while k > 1 and self.array[k][1] < self.array[k//2][1]:
            self.swap(k, k//2)
            k = k // 2


    def sink(self, k):
        '''
        @purpose: Maintains the heap order by sinking the item
        @param: k - index of the item to sink
        @complexity: O(log n) where n is the number of items
        @precondition: PriorityQueue initialised
        @postcondition: The item is placed at position fulfilling heap order
        '''
        while 2*k <= self.count:
            child = self.smallest_child(k)
            if self.array[k][1] <= self.array[child][1]:
                break
            self.swap(child, k)
            k = child

    def smallest_child(self, k):
        '''
        @purpose: Get the index of the smallest priority child
        @param: k - index of the current root node
        @complexity: O(1)
        @precondition: PriorityQueue initialised
        @postcondition: Returns the index of the child with smallest priority
        '''
        if 2*k == self.count or self.array[2*k][1] < self.array[2*k+1][1]:
            return 2*k
        else:
            return 2*k + 1

    def serve(self):
        '''
        @purpose: Serves the front of the priority queue
        @param: None
        @complexity: O(log n) where n is the number of items
        @precondition: PriorityQueue initialised
        @postcondition: Returns the (item,priority) with min priority
        '''
        if self.count != 0:
            item = self.array[1]
            self.swap(1, self.count)
            self.count -= 1
            self.sink(1)
            return item
        else:
            raise IndexError('Heap empty')

    def peek(self):
        '''
        @purpose: Peeks at the front of the priority queue
        @param: None
        @complexity: O(1)
        @precondition: PriorityQueue initialised
        @postcondition: Returns the item with min priority
        '''
        if self.count != 0:
            return self.array[1]

    def print_all(self):
        '''
        @purpose: Prints out all items
        @param: k - index of the item to rise
        @complexity: O(n) where n is the number of items
        @precondition: PriorityQueue initialised
        @postcondition: Prints out all items in the array
        '''
        if self.count == 0:
            raise IndexError('Heap empty')
        else:
            print("\n[Item, Priority]")
            for i in range(1,len(self)+1):
                print(self.array[i])

    def max_priority(self):
        '''
        @purpose: Finds the maximum priority
        @param: None
        @complexity: O(n) where n is the number of items
        @precondition: PriorityQueue initialised
        @postcondition: Returns the max priority
        '''
        max = 0
        for i in range(1,len(self)+1):
            if self.array[i][1] > max:
                max = self.array[i][1]
        return max

    def reset(self):
        # resets the priority queue
        self.count = 0
        self.array = [None]

#######

def menu_append(pq):
    try:
        item = int(input("Integer: "))
        pq.add(item, pq.max_priority()+1)
    except ValueError:
        print("Integer only.")

def menu():
    # menu function
    quit = False
    pq = PriorityQueue()
    while not quit:
        try:
            print("\n1. Append")
            print("2. Serve")
            print("3. Print")
            print("4. Size")
            print("5. Quit")
            print("6. Tests")
            cmd = int(input("Command: "))
            if cmd == 5:
                quit = True
            elif cmd == 1:
                menu_append(pq)
            elif cmd == 2:
                print(pq.serve()[0])
            elif cmd == 3:
                pq.print_all()
            elif cmd == 4:
                print(len(pq))
            elif cmd == 6:
                test_t1()
            else:
                raise ValueError

        except AttributeError:
            print("Invalid command.")
        except IndexError:
            print("Priority Queue empty.")
        except TypeError:
            print("Please insert integer for priority.")


def test_t1():
    mheap = PriorityQueue()
    print("Adding 2,2")
    mheap.add(2,2)
    print("Adding 3,3")
    mheap.add(3,3)
    print("Adding 5,5")
    mheap.add(5,5)
    print("Adding 1,1")
    mheap.add(1,1)
    print("Adding 3,3")
    mheap.add(3,3)
    print("Adding 2,2")
    mheap.add(2,2)
    print("Adding 9,9")
    mheap.add(9,9)
    print("Adding 0,0")
    mheap.add(0,0)
    print("Adding 1,1")
    mheap.add(1,1)
    print("Adding 1,a")
    try:
        mheap.add(1,'a')
    except TypeError:
            print("> Please insert integer for priority.")
    print("Adding 'a',3")
    mheap.add('a',3)

    print("\nSize of queue: " + str(len(mheap)))

    print("\nPriority Queue:")
    print(mheap.array)

    print("\nTesting serve(), it should print items in the order of the priority ")
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])
    print(mheap.serve()[0])


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        pass
