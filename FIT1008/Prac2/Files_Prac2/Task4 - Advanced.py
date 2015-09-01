"""
Advanced Question
@purpose This program determines the solvability of an n-puzzle
@author Loh Hao Bin 25461257
@since 20140803
@modified 20140806
@Precondition: The user inputs a configuration of n-puzzle
@Postcondition: The program returns whether the puzzle is solvable.
@Complexity: O(n^2)
"""

def print_current_state():
    """
    @purpose Printing current board
    """
    for i in range(rows):
        print(" |".join(puzzle[i]))

"""MAIN BLOCK BEGIN"""

print("This program allows you to input your own configuration of a n-puzzle and determine whether it is solvable. "
      "Please input the numbers of the squares accordingly, and use the largest number for representing the blank space.")

try:
    rows = int(input(">How many rows? "))
    column = int(input(">How many columns? "))

    if rows > 0 and column > 0:
        #initializinggggg
        num = (rows * column)
        puzzle = []
        compare_list = []
        position = []

        for i in range(rows):
            puzzle.append([])   #making new row
            for j in range(column):
                #looping to input
                config_input = str(input("Please input number for row " + str(i) + " column " + str(j) + ": "))
                compare_list.append(config_input)   #using a 1D array to simplify comparison later
                puzzle[i].append(config_input.rjust(2))     #2D array for presentation
                if config_input == str(num):
                    #get current position of the blank space
                    position.append(i)
                    position.append(j)


        #print(compare_list)
        #print(position)

        #Calculating swaps
        swaps = 0
        for x in range(num):
            for y in range(x,-1,-1):
                if int(compare_list[x]) < int(compare_list[y]) :
                    #calculate the number of previous tiles larger than current tile
                    swaps += 1
                    #print(".")

        #calculate taxicab metric
        y_delta = rows - 1 - position[0]
        x_delta = column - 1 - position[1]
        delta = y_delta + x_delta

        #display results
        print("\n")
        print_current_state()
        print("\n" + str(swaps) + " swaps")
        print(str(delta) + " city-distance")
        print(str(swaps + delta) + " total")

        #determine solvability by parity of total, and display
        if (swaps + delta) % 2 == 0:
            print("Even parity. This puzzle is solvable.")
        else:
            print("Odd parity. This puzzle is unsolvable.")

    else:
        print("Please enter a positive value greater than zero.")

except ValueError:
    print("Please enter valid value(s).")