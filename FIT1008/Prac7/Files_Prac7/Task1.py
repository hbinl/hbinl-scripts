"""
FIT1008 Prac 7 Task 1
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: Stack ADT
@created 20140913
@modified 20140914
"""

class Stack:
    def __init__(self,size):
        """
        @purpose: To initialise a stack
        @complexity:
        Best & Worst Case: O(n) where n is the size
        @parameter Size: where "size" is the size of the stack
        @precondition: Size has to be a positive value
        @postcondition: An array for the stack
        """
        if size > 0:
            self.the_array = size*[None]
            self.item_count = 0
            self.top = -1
        else:
            raise AssertionError

    def is_empty(self):
        """
        @purpose: To check if the stack is empty
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: The Stack class has been initialised
        @postcondition: return True/False
        """
        return len(self) == 0

    def is_full(self):
        """
        @purpose: To check if the stack is full
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: The Stack class has been initialised
        @postcondition: return True/False
        """
        return len(self) >= len(self.the_array)

    def __len__(self):
        """
        @purpose: To give the number of items in the stack
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: The Stack class has been initialised
        @postcondition: return the number of item in the stack
        """
        try:
            return self.item_count
        except AttributeError:
            return 0

    def __str__(self):
        """
        @purpose: To print all the item in the stack in reverse order without manipulating the stack structure
        @complexity:
            Best & Worst Case: O(N) where n is the number of items in the stack
        @parameter: None
        @precondition: The Stack class has been initialised
        @postcondition: prints out all the items in the stack in reverse order, the structure of the stack is still preserve
        """
        if self.is_empty() == False:
            final = str(self.the_array[self.top])
            for i in range(self.top-1, -1, -1):
                final = final + ' ' + str(self.the_array[i])
            return final
        else:
            return('Stack empty.')

    def push(self, item):
        """
        @purpose: To push item into the stack
        @complexity:
        Best & Worst Case: O(1)
        @parameter: item: the item to be pushed into stack
        @precondition: The Stack class has been initialised
        @postcondition: A stack with the new item in it
        """
        if self.is_full() == False:
                    self.top += 1
                    self.the_array[self.top] = item
                    self.item_count += 1
        else:
            print('Stack full.')


    def pop(self):
        """
        @purpose: To pop item off the stack
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: The Stack class has been initialised
        @postcondition: A new stack with the top item removed
        """
        if self.is_empty() == False:
            top_item = self.the_array[self.top]
            self.the_array[self.top] = None
            self.top -= 1
            self.item_count -= 1
            return top_item
        else:
            return 'Stack empty.'

    def peek(self):
        return self.the_array[self.top]

    def listform(self):
        return self.the_array


def menu():
    """
        @purpose: To print the menu
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
    """
    try:
        quit = False
        size = int(input("Stack size: "))
        stk = Stack(size)
        while not quit:
            print('\n1. Push')
            print('2. Pop')
            print('3. Print')
            print('4. Size')
            print('5. Quit')
            cmd = int(input('Command:'))

            if cmd == 1:
                try:
                    item = int(input("Please input an integer: "))
                    stk.push(item)
                except ValueError:
                    print("Please enter integer only into the stack.")
            elif cmd == 2:
                print(stk.pop())
            elif cmd == 3:
                print(str(stk))
            elif cmd == 4:
                print('Size: ' + str(len(stk)))
            elif cmd == 5:
                quit = True
            else:
                print("Please input a valid command.")

    except AssertionError:
        print("Invalid size. Please input a size > 0.")

    except ValueError:
        print("Invalid input, please input a valid command.")

def test_class_stack():
    stk = Stack(5)

    print('Testing 1. Push: items = [3,5,6,2]')
    stk.push('3')
    stk.push('5')
    stk.push('6')
    stk.push('2')
    print('Stack: ' + str(stk))

    print('\nTesting 2. Pop')
    x = stk.pop()
    print('Pop = ' + str(x))
    print('Stack: ' + str(stk))

    y = stk.pop()
    print('\nTesting 3. Print')
    print('Stack: ' + str(stk))

    print('\n Testing 4. Size')
    print('Size: ' + str(len(stk)))

    print(stk.listform())

if __name__ == "__main__":
    try:
        test_class_stack()
        print('\n')
        menu()
    except KeyboardInterrupt:
        print('User stopped the program.')