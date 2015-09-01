"""
Task 3
@purpose This program is a game of 15-puzzle.
@author Loh Hao Bin 25461257
@since 20140803
@modified 20140806

"""

def menu():
    """
    @purpose For printing the menus
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
    @Complexity: O(1)
    """
    temp = puzzle[ old[0] ][ old[1] ]
    puzzle[ old[0] ][ old[1] ] = puzzle[ new[0] ][ new[1] ]
    puzzle[ new[0] ][ new[1] ] = temp
    return puzzle

def Start_Screen():
    """
    @purpose: For displaying a welcome screen.
    @parameters: none
    """
    begin = input("Welcome to the 15-puzzle game. \nPress enter to begin.\n ")


"""START Main Block"""
try:
    Start_Screen()
    puzzle = [
        [' 1', ' 2', ' 3', ' 4'],
        [' 5', ' 6', ' 7', ' 8'],
        [' 9', '10', '11', '12'],
        ['13', '14', '15', ' X']
    ]               #Default board
    position = [3,3]    #default position
    quit = False

    while not quit:
        try:
            print_current_state()
            menu()
            command = str(input("Type 'quit' to exit. \n>> Your next move: "))
            old_position = list(position)

            if command == "1":
                #Check if out of bound
                if position[0] > 0:
                    position[0] -= 1
                    print("Up")
                    swap_blocks(old_position, position)
                else:
                    messages(0)

            elif command == "2":
                #Check if out of bound
                if position[0] < 3:
                    position[0] += 1
                    print("Down")
                    swap_blocks(old_position, position)
                else:
                    messages(0)

            elif command == "3":
                #Check if out of bound
                if position[1] > 0 :
                    position[1] -= 1
                    print("Left")
                    swap_blocks(old_position, position)
                else:
                    messages(0)

            elif command == "4":
                #Check if out of bound
                if position[1] < 3:
                    position[1] += 1
                    print("Right")
                    swap_blocks(old_position, position)
                else:
                    #Display illegal move out of bound
                    messages(0)

            elif command == "quit":
                quit = True

            else:
                #Display invalid command
                messages(1)

            #print(old_position)
            #print(position)
            print("\n" + "-"*40)

        except ValueError:
            print("\nInvalid value.")
        except TypeError:
            print("\nInvalid value.")

except KeyboardInterrupt:
    print("\nProgram ended.")