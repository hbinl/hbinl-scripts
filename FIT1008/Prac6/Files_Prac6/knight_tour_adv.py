"""
FIT1008 Prac 6 Advanced Task
Loh Hao Bin 25461257
@purpose: Knight in Chess
            File: The columns
            Rank: The rows
@created 20140831
@modified 20140831
"""

class Tour:
    def __init__(self,y,x):
        self.board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        self.knight_history = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        self.current_pos = [y,x]
        self.knight_history[y][x] = 1
        self.board[y][x] = 1
        self.nextcount = 2
        self.start_pos = [y,x]

    def next_moves(self,p):
        """
        @purpose To return a list of next possible legal moves
        @complexity:
            Best & Worst Case: O(n) where n is the dimension of the board
        @parameter p: Option -
        2 for next legal moves including starting
        1 for all possible moves, 0 for only next legal moves
        @precondition The Tour class has been initialised
        @postcondition returns a list of next possible legal moves for Knight
        """
        next = [
            (-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)
        ]
        final = []
        for i in range(len(next)):
            possible = []
            y = self.current_pos[0] + next[i][0]
            x = self.current_pos[1] + next[i][1]

            if y >= 0 and x >=0 and y <= 7 and x <= 7:
                if p == 0 or p == 2:
                    if self.knight_history[y][x] == 0:
                        possible.append(y)
                        possible.append(x)
                        final.append(possible)
                    if p == 2:
                        if self.knight_history[y][x] == 1:
                            possible.append(y)
                            possible.append(x)
                            final.append(possible)
                else:
                    possible = []
                    possible.append(y)
                    possible.append(x)
                    final.append(possible)

        return final

    def display(self):
        """
        @purpose To display the current chess board state
        @complexity:
            Best & Worst Case: O(n^2) where n is the dimension of the board
        @parameter none
        @precondition The Tour class has been initialised
        @postcondition prints out the current board state
        """
        print("\n", end="  ")
        for i in range(8):
            print(i, end=" ")
        print()
        for i in range(8):
            print(i, end=" ")
            for j in range(8):
                if (self.board[i][j] == 1) and (self.knight_history[i][j] != 0):
                    print("K", end=" ")
                elif (self.knight_history[i][j] != 0) and (self.board[i][j] == 0):
                    print("*", end=" ")
                else:
                    print(0, end=" ")
            print()

    def display_history(self):
        """
        @purpose To display the current chess board history
        @complexity:
            Best & Worst Case: O(n^2) where n is the dimension of the board
        @parameter none
        @precondition The Tour class has been initialised
        @postcondition prints out the current board history
        """
        print("\n", end="   ")
        for i in range(8):
            print(str(i).center(2), end=" ")
        print()
        for i in range(8):
            print(i, end="  ")
            for j in range(8):
                if (self.board[i][j] == 1) and (self.knight_history[i][j] != 0):
                    print("K".center(2), end=" ")
                else:
                    print(str(self.knight_history[i][j]).center(2), end=" ")
            print()
        print()

    def move(self,y,x):
        """
        @purpose To move the Knight to new position
        @complexity: O(1)
        @parameter
            x: the File to move to
            y: the Rank to move to
        @precondition The Tour class has been initialised, and a valid x/y value passed
        @postcondition current_pos is modified to new Knight position, and Knight's move history
                        is left in knight_history, and the current board is printed out
        """

        if (x >= 0 and x <= 7) and (y >= 0 and y <= 7):
                #remember current Knight position
                old_x = self.current_pos[1]
                old_y = self.current_pos[0]
                self.board[old_y][old_x] = 0

                #set new Knight Position
                self.current_pos = [y,x]
                self.board[y][x] = 1
                self.knight_history[y][x] = self.nextcount
                self.nextcount += 1
        else:
            raise ValueError


#FUNCTIONSS

def start():
    """
    @purpose To reset the board and read a new start for Knight
    @complexity:
        Best & Worst Case: O(1)
    @parameter none
    @precondition The Tour class has been initialised, and valid positions
                for knight are inputted
    @postcondition A new board is generated with new Knight position
    """
    try:

        posY = int(input("Starting Y (Rank): "))
        posX = int(input("Starting X (File): "))

        if (posX >= 0 and posX <= 7) and (posY >= 0 and posY <= 7):
            global board
            board = Tour(posY,posX)
        else:
            raise IndexError

    except ValueError:
        print("Please input a valid File and Rank.")
    except IndexError:
        print("Please input a valid File and Rank within range.")


def positions():
    """
    @purpose To display the list of next possible legal positions, and
            allow the user to move to them
    @complexity:
        Best & Worst Case: O(n^2) where n is the dimension of the board
    @parameter none
    @precondition The Tour class has been initialised
    @postcondition Displays a list of next possible legal moves, and
                    allow for user to move Knight to the position in list
    """
    try:
        next = board.next_moves(0)

        if len(next) > 0:
            for i in range(len(next)):
                print(str(i+1) + ". " + str(next[i]))

            user_move = int(input("Next move: ")) - 1
            if user_move >= 0 and user_move < len(next):
                posY = next[user_move][0]
                posX = next[user_move][1]
                board.move(posY,posX)
            else:
                raise IndexError

        else:
            print("There are no legal moves available.")

    except IndexError:
        print("Please choose from the valid positions above.")
    except ValueError:
        print("Please choose from the valid positions above.")

def undo():
    """
    @purpose To undo the last move
    @complexity:
        Worst Case: O(n) where n is size of previous moves
        Best Case: O(1) when there is nothing to undo
    @parameter none
    @precondition The Tour class has been initialised
    @postcondition
        - Undoes the current knight_history
        - Reverse current knight position in board
        - Decrements the nextcount
    """
    if board.nextcount > 2:
        prev = board.next_moves(1)
        #print(prev)
        max = 1
        max_x = board.current_pos[1]
        max_y = board.current_pos[0]

        for i in range(len(prev)):
            y = prev[i][0]
            x = prev[i][1]
            if board.knight_history[y][x] >= max:
                max = board.knight_history[y][x]
                max_y = y
                max_x = x

        old_x = board.current_pos[1]
        old_y = board.current_pos[0]
        board.board[old_y][old_x] = 0
        board.knight_history[old_y][old_x] = 0

        board.current_pos = [max_y,max_x]
        board.board[max_y][max_x] = 1
        board.nextcount -= 1
    else:
        print("Nothing to undo.")

"""
def backtracking(partialSolution, rem):
    if len(partialSolution) == (64 - (rem - 2)):
        print(".", end="")
        if partialSolution[len(partialSolution)] == board.start_pos:
            print(partialSolution)
            raise Exception
    else:
        possibleItems = board.next_moves(2)
        k = 0
        while k < len(possibleItems):
            x = possibleItems[k]
            partialSolution.append(x)
            board.move(x[0],x[1])
            backtracking(partialSolution,rem)
            undo()
            partialSolution.pop()
            k += 1
"""

def solution():
    """
    @purpose Based on Warnsdorff's Heuristic, at every point the algorithm will
            choose to go to the path with least next possible legal moves
            Forms an open tour
    @complexity:
        Worst Case: O(n * m) where n is the size of the board, and m is
                    the length of next possible moves for current position
    @parameter none
    @precondition The Tour class has been initialised
    @postcondition Returns the sequence of moves of Knight's Tour
    """
    final = []
    for i in range(64 - board.nextcount + 1):
        # We iterate only the amount of times remaining based on nextcount

        if len(final) < 63:
            possibleItems = board.next_moves(0)
        # calculate next moves and return into a list
        k = 0
        compare = 8
        least = 0
        while k < len(possibleItems):
            #iterate through current next moves
            x = possibleItems[k]
            board.move(x[0],x[1])
            # simulate a move
            temp = board.next_moves(0)
            # then calculate next move for the current location
            # if next move for current location is less, keep track
            if len(temp) < compare:
                compare = len(temp)
                least = k
            undo()
            # revert to previous position
            k += 1
        go = possibleItems[least]
        # append the valid path (aka the least path next)
        final.append(go)
        # move there and looooop
        board.move(go[0],go[1])
    return final


def menu():
    """
    @purpose To display the menu
    @complexity: O(1)
    @parameter None
    @precondition None
    @postcondition
    """
    try:
        print("\n1. Quit")
        print("2. Start")
        print("3. Position")
        print("4. Solution")
        print("5. Undo")
        ans = int(input("Command: "))

        if ans == 1:
            print("User stopped the program.")
            global quit
            quit = True

        elif ans == 2:
            start()

        elif ans == 3:
                positions()
        elif ans == 4:
            try:

                # store starting position
                first_pos = board.current_pos
                partialSolution = solution()
                # calculate
                # prepend starting position
                partialSolution.insert(0,first_pos)
                print(len(partialSolution))
                # print history board
                board.display_history()
                print("Sequence of Knight's Tour from current position: \n"
                      + str(partialSolution))
                """
                partialSolution = []
                partialSolution.append(board.current_pos)
                backtracking(partialSolution, board.nextcount)
                """

            except IndexError:
                print("Error: There's no solution from this position onwards.")
            except Exception:
                print("Done.")
            #quit = True

        elif ans == 5:
            undo()

        else:
            raise ValueError

    except ValueError:
        print("Please input a valid command.")


if __name__ == "__main__":
    try:
        progress = 1
        global quit
        quit = False        #set flag
        board = Tour(0,1)   #initialise class Tour
        print("Welcome to Knight Tour. " +
              "\nPosition: [Rank y, File x]")
        while not quit:
            print("-"*30)
            board.display()
            menu()

    except KeyboardInterrupt:
        print("\nUser stopped the program.")