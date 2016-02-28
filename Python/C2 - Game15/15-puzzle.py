"""
Task 3 - HOF
@purpose This program is a game of 15-puzzle.
@author Loh Hao Bin 25461257
@since 20140803
@modified 20140806

"""
from random import shuffle

def menu():
    """
    @purpose: Printing menus
    @Parameters: None
    @Complexity: O(1)
    """
    print("\n1. Up")
    print("2. Down")
    print("3. Left")
    print("4. Right")

def print_current_state():
    """
    @purpose Printing current board
    @Parameters: None
    """
    for i in range(4):
        print(" | ".join(puzzle[i]))

def messages(n):
    """
    @purpose For printing out custom error messages.
    @parameter:
            n: The message code to be displayed
    @precondition: The function is passed a message code
    @postcondition: The function displays the requested message.
    """
    if n == 0:
        print("Illegal move.")
    elif n == 1:
        print("Invalid command.")


def swap_blocks(old, new):
    """
    @purpose For swapping the blank space, and the target block
    @parameters:
            old: the old position of blank space
            new: the new target position of blank space
    @precondition: The function is passed position coordinates of blank space, and the target tile
    @postcondition: The blank space is swapped with the tile in the target position
    """
    temp = puzzle[ old[0] ][ old[1] ]
    puzzle[ old[0] ][ old[1] ] = puzzle[ new[0] ][ new[1] ]
    puzzle[ new[0] ][ new[1] ] = temp
    return puzzle


def rand_board():
    """
    @purpose For generating a random board
    """

    #generating a number list, then random.shuffle it, then pop it to the 2d array
    numlist = []
    for x in range(1,17):
        numlist.append(x)
    shuffle(numlist)

    numlist.reverse()
    #Calculating swaps, from Advanced.py
    swaps = 0
    for x in range(16):
        for y in range(x,-1,-1):
            if int(numlist[x]) < int(numlist[y]) :
                #calculate the number of previous tiles larger than current tile
                swaps += 1
    numlist.reverse() #have to reverse back due to how .pop() works

    for i in range(4):
        puzzle.append([])
        for j in range(4):
            item = str(numlist.pop()).rjust(2)
            if item == "16":
                position.append(i)
                position.append(j)
            puzzle[i].append(item)

    #calculate taxicab metric
    y_delta = 4 - 1 - position[0]
    x_delta = 4 - 1 - position[1]
    delta = y_delta + x_delta

    #parity check, if fails: generate again
    if (delta+swaps) % 2 != 0:
        del puzzle[:]
        del position[:]
        rand_board()
    else:
        puzzle[position[0]][position[1]] = " X"

def Start_Screen():
    """
    @purpose: For displaying a welcome screen.
    @parameters: none
    """
    begin = input("Welcome to the 15-puzzle game. \nPress Enter to begin. ")


"""START Main Block"""
try:
    Start_Screen()
    print("\nGenerating new random board...")
    quit = False    #initialize...
    puzzle = []
    position = []
    rand_board()

    while not quit:
        try:
            print_current_state()
            menu()
            command = str(input("Type 'quit' to exit, and 'reset' to restart. \n>> Your next move: "))
            old_position = list(position)

            if command == "1":
                if position[0] > 0:
                    position[0] -= 1
                    print("Up")
                    swap_blocks(old_position, position)
                else:
                    messages(0)

            elif command == "2":
                if position[0] < 3:
                    position[0] += 1
                    print("Down")
                    swap_blocks(old_position, position)
                else:
                    messages(0)

            elif command == "3":
                if position[1] > 0 :
                    position[1] -= 1
                    print("Left")
                    swap_blocks(old_position, position)
                else:
                    messages(0)

            elif command == "4":
                if position[1] < 3:
                    position[1] += 1
                    print("Right")
                    swap_blocks(old_position, position)
                else:
                    messages(0)

            elif command == "reset":
                print("\nGenerating new random board...")
                puzzle = []
                position = []
                rand_board()

            elif command == "quit":
                quit = True

            else:
                messages(1)

            print("\n" + "-"*40)

        except ValueError:
            print("\nInvalid value.")
        except TypeError:
            print("\nInvalid value.")

except KeyboardInterrupt:
    print("\nProgram ended.")