"""
FIT1008 Prac 8 Task 2
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: Army Classes
@created 20140918
@modified 20140918
"""

from Task1 import *
#take input 1st, split it, check if input is positive, push into the stack, check if they all < 20#

class Army:
    def __init__(self, name='', inp=''):
        """
        @purpose: To get user's name, player's army
        @complexity:
            Best Case: O(1), when the army input is invalid, no stack
            Worst Case: O(N^2), where n is the number of units
        @parameter:
            name: Name of the player of this army, if empty, it will ask for input
            inp: Units of the army in S A C format, if empty, it will ask for input
        @precondition: None
        @postcondition: An army object is created containing a stack of units
        """
        if name == '':
            name = input("Player Name: ")
        self.user_name = name

        quit = False
        while not quit:
            try:
                if inp == '':
                    print("\n" + self.user_name + ", choose your army as S A C")
                    print("where S is the number of soldiers")
                    print("      A is the number of archers")
                    print("  and C is the number of cavalry")
                    inp = input("Current funds: $20 \nInput: ")
                inp = inp.split()  # returns the input as a list

                if len(inp) != 3:  # only accept input of 3 (size of list has to be 3)
                    print("Please input 3 numbers only, separated by space.")
                    raise AttributeError

                stk_size = 0
                for i in range(len(inp)):
                    if int(inp[i]) < 0:  # check if input is a positive
                        raise ValueError
                    stk_size += int(inp[i])  # setting the stack size as sum of army

                self.the_array = stk_size * [None]
                self.item_count = 0
                self.top = -1

                for i in range(len(inp)-1, -1, -1):  # push the army into the stack
                    for j in range(int(inp[i])):
                        if i == 2:
                            self.push(Cavalry())
                        elif i == 1:
                            self.push(Archer())
                        elif i == 0:
                            self.push(Soldier())
                if len(self) <= 0:
                    raise ValueError

                total_cost = 0
                for unit in self.the_array:  # loops through the units(Soldier, Archer, Calvary) in the stack
                    total_cost += unit.getCost()  # sums the unit price according to the  object "unit"(S, A, C)
                    if total_cost > 20:  # checking if the army cost it <= 20
                        print("Not enough funds.")
                        raise AttributeError

                print("\nPlayer: " + self.player_name())
                print(str(self))
                print("Funds left: $" + str(20-total_cost))
                quit = True

            except AttributeError:
                inp = ''
            except ValueError:
                print("Please input only positive integers > 0.")
                inp = ''

    def player_name(self):  # function to return player's name
        """
        @purpose: to return player's name
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance user_name has to be initialize
        @postcondition: Returns the user's name
        """
        return str(self.user_name)

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
                final = final + '\n' + str(self.the_array[i])
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
        """
        @purpose: To get the top item in the stack
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: The Stack class has been initialised
        @postcondition: Returns the top item in stack
        """
        return self.the_array[self.top].unit_name

def army_test_function():
    print("_" * 30)
    print("Input = 1 2 3, it should work properly")
    player = Army("Wen Jie", "1 2 3")

    print("_" * 30)
    print("\nInput = 0 0 0, all 0, it should ask for another input")
    player = Army("Wen Jie", "0 0 0")

    print("_" * 30)
    print("\nInput = -1 0 2, negative input it should ask for another input")
    player = Army("Wen Jie", "-1 0 2")

    print("_" * 30)
    print("\nInput = 0, length too short, it should ask for another input")
    player = Army("Wen Jie", "0")

    print("_" * 30)
    print("\nInput = 9 9 9, too many units, not enough funds")
    player = Army("Wen Jie", "9 9 9")

    print("_" * 30)
    print("\nInput = 1 2 3 4 5, length too long")
    player = Army("Wen Jie", "1 2 3 4 5")

    print("_" * 30)
    print("\nInput = a, invalid input")
    player = Army("X", "a")

    print("_" * 30)
    print("\nNo input")
    player = Army()

def army_test_menu():
        """
        @purpose: To test the army menu
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Class Army initialize
        @postcondition: Returns the stack of army, cost left, for player 1 and 2
        """
        print("Welcome to the Clans of Clash! ")
        print("\nPlayer 1")
        p1 = Army()
        print("\nPlayer 2")
        p2 = Army()


if __name__ == "__main__":
    army_test_function()
    #army_test_menu()