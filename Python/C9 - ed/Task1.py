"""
FIT1008 Prac 9 Task 1
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: Linked List
@created 20141002
@modified 20141003
"""

class Node:
    def __init__(self, item = None, link_next = None):
        """
            @purpose: Creates a node
        """
        self.item = item
        self.next = link_next

    def __str__(self):
        """
        @purpose: Overloads the str on Node objects, such that it returns the item contained
                inside the node
        @complexity: O(1)
        """
        return str(self.item)

class LinkedList:
    def __init__(self):
        """
        @purpose: Creates a linked list
        """
        self.head = None
        self.count = 0

    def is_empty(self):
        """
        @purpose: To check if the linked list is empty
        @parameter: None
        @complexity: O(1)
        @precondition: Linked list object initialised
        @postcondition: Returns True/False depending on empty or not
        """
        return self.count == 0

    def is_full(self):
        """
        @purpose: To check if the linked list is full, which is always False
        @parameter: None
        @complexity: O(1)
        @precondition: Linked List object initialised
        @postcondition: Returns False
        """
        return False

    def reset(self):
        """
        @purpose: Reinitialise the linked list
        @parameter: None
        @complexity: O(1)
        @precondition: Linked List object initialised
        @postcondition: Linked List cleared and returned to initial state
        """
        self.__init__()

    def __len__(self):
        """
        @purpose: Returns the length of the linked list
        @parameter: None
        @complexity: O(1)
        @precondition: Linked List object initialised
        @postcondition: Returns the count of items inside the list
        """
        return self.count

    def _getNode(self,index):
        """
        @purpose: Get a specified node
        @parameter: index: the index of the node to be obtained
        @complexity:
                Best Case: O(1) when index is invalid
                Worst Case: O(n) where n is the length of the list
        @precondition: Linked List object initialised
        @postcondition: Returns the item requested
        """
        node = self.head

        for _ in range(index):
            node = node.next

        return node

    def insert(self, index, item):
        """
        @purpose: Insert an item at the specified index
        @parameter: index: The index to be inserted at
                    item: The item to be inserted
        @complexity: Worst Case O(n) where n is the index
                     Best Case O(1) when invalid index is given
        @precondition: Linked List object initialised
        @postcondition: The item is inserted at the specified index in the list
        """

        index = int(index)

        #if index is negative, wrap around
        if index < 0:
            index = len(self) + index + 1
        elif index > len(self):
        #if index exceed length, put at the end
            index = len(self)

        if index == 0:
            #if insert at position 0
            self.head = Node(item, self.head)
        else:
            node = self._getNode(index-1)
            node.next = Node(item, node.next)

        self.count += 1


    def delete(self, index = ''):
        """
        @purpose: Deletes item at index
        @parameter: index (optional): index to be deleted, if empty, deletes everything
        @complexity: Best Case: O(1) when it resets
                     Worst Case: O(n) where n is the index
        @precondition: Linked List object initialised
        @postcondition: The item deleted from the specific index
        """
        if index == '':
            self.reset()
            return

        index = int(index)
        if self.is_empty() == True or index < 0 or index >= len(self):
            raise IndexError

        if index == 0:
            self.head = self.head.next
        else:
            node = self._getNode(index-1)
            node.next = node.next.next
            #node.next = self._getNode(index+1)

        self.count -= 1

    def append(self, item):
        """
        @purpose: Appends item at the end of linked list
        @parameter: item: the item to be appended
        @complexity: Best Case: O(1) when list is empty
                     Worst Case: O(n) where n is index traversed
        @precondition: Linked List object initialised
        @postcondition: The item is added to the end of the list
        """
        if self.is_empty() == True:
            self.head = Node(item, None)

        else:
            node = self._getNode(len(self)-1)
            node.next = Node(item, None)

        self.count += 1

    def return_content(self, index = ''):
        """
        @purpose: Returns the content of a specific node at index as a string
        @parameter: index (optional): the index to be returned, else returns all items
        @complexity: Best Case: O(1) when it is empty
                     Worst Case: O(n) where n is the length of list
        @precondition: Linked List object initialised
        @postcondition:Returns a string of the nodes requested
        """
        if self.is_empty() == True:
            return ""

        output = None

        if index == '':
            #if no parameter is given
            output = str(self.head.item)
            node = self.head.next
            #loop through whole list
            for _ in range(1,len(self)):
                output = output + str(node.item)
                node = node.next
        else:

            #check if index in range
            if int(index) < len(self) and int(index) >= 0:
                node = self._getNode(int(index))
                output = node.item
            else:
                raise IndexError

        return output.rstrip()



def ll_menu():
    """
        @purpose: Just a menu to test linked lists class methods

    """
    print("Linked List test menus.")
    quit = False
    list = LinkedList()

    while not quit:
        try:
            print("\n1. Insert Num")
            print("2. Delete Num")
            print("3. Print Num")
            print("4. Quit")
            print("5. Test Function")
            cmd = int(input("Command: "))

            if cmd == 1:

                #Insert Num
                try:
                    index = int(input("Insert Index: "))
                    item = input("Item: ")
                    list.insert(index, item)
                except ValueError:
                    print("Please insert integer index only.")

            elif cmd == 2:
                #Delete Num
                try:
                    index = input("Delete Index: ")
                    list.delete(index)
                except ValueError:
                    print("Please insert a valid index.")
                except IndexError:
                    print("List is empty or index out of range.")

            elif cmd == 3:
                #Print Num
                try:
                    position = input("Print line at: ")
                    print(list.return_content(position))

                except IndexError:
                    print("Index out of range.")
                except ValueError:
                    print("Please insert a valid index.")

            elif cmd == 4:
                #Quit
                quit = True

            elif cmd == 5:
                    #Test
                    test_function()
                    quit = True

            else:
                #if invalid command
                raise ValueError

        except ValueError:
            print("Please insert a valid command.")


### TEST FUNCTIONS
def test_function():
    print("="*30)
    print("\n> Test Insert function")
    test_insert()
    print("="*30)
    print("\n> Test Append function")
    test_append()
    print("="*30)
    print("\n> Test Delete function")
    test_delete()


def test_append():
    test_list = LinkedList()
    #Test Append
    print("Append 3, 4 and 9")
    test_list.append(3)
    print(test_list.return_content())
    test_list.append(4)
    print(test_list.return_content())
    test_list.append(9)
    print(test_list.return_content())



def test_insert():
    test_list = LinkedList()
    #Test Insert
    print("\nInsert 5 at index 0")
    test_list.insert(0,5)
    print(test_list.return_content())

    print("\nInsert 5 at index 0")
    test_list.insert(0,688558)
    print(test_list.return_content())

    print("\nInsert 4 at index 6")
    test_list.insert(6,4)
    print(test_list.return_content())

    print("\nInsert 9 at index -1")
    test_list.insert(-1,9)
    print(test_list.return_content())

    print("\nInsert b at index 4")
    test_list.insert(4,'b')
    print(test_list.return_content())

    print("\nInsert 5 at index a")
    try:
        test_list.insert('a',5)
        print(test_list.return_content())
    except ValueError:
        print("Please insert integer index only.")

def test_delete():
    test_list = LinkedList()
    try:
        test_list.delete(2)
    except IndexError:
        print("?")


    test_list.append(1)
    test_list.append(2)
    test_list.append(3)
    test_list.append(4)
    print(test_list.return_content())

    print("\nDelete index 2")
    test_list.delete(2)
    print(test_list.return_content())
    print("\nDelete index a")
    try:
        test_list.delete('a')
    except ValueError:
        print("Please insert a valid index.")
    print(test_list.return_content())
    print("\nCalling Delete without giving num")
    test_list.delete()
    print(test_list.return_content())



if __name__ == "__main__":
    try:
        ll_menu()
    except KeyboardInterrupt:
        print()