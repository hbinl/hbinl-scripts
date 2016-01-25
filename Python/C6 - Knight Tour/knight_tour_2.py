"""
FIT1008 Prac 6 Task 2
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: Knight in Chess
            File: The columns
            Rank: The rows
@created 2014831
@modified 20140903
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

    def display(self,n):
        """
        @purpose To display the current chess board state
        @complexity:
            Best & Worst Case: O(n^2) where n is the dimension of the board
        @parameter n: where n is the dimension of the board
        @precondition The Tour class has been initialised
        @postcondition prints out the current board state
        """
        print("\n", end="  ")
        for i in range(n):
            print(i, end=" ")

        print()

        for i in range(n):
            print(i, end=" ")
            for j in range(n):
                if (self.board[i][j] == 1) and (self.knight_history[i][j] == 1):
                    print("K", end=" ")
                elif self.knight_history[i][j] == 1 and (self.board[i][j] == 0):
                    print("*", end=" ")
                else:
                    print(0, end=" ")
            print()

    def move(self,x,y):
        """
        @purpose To display the current chess board state
        @complexity:
            Best Case: O(1) - x and y out of bound
            Worst Case: O(1)
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
                self.knight_history[y][x] = 1
        else:
            raise ValueError

    def next_moves(self):
        """
        @purpose To generate next possible moves for Knight
        @complexity:
            Best Case: O(1) - All location invalid
            Worst Case: O(1) - All location valid
        @parameter: none
        @precondition: Tour class initialised
        @postcondition Returns a list of possible legal moves
        """
        next = [
            (-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)
        ]
        final = []
        for i in range(len(next)):
            possible = []
            y   =  self.current_pos[0] + next[i][0]
            x   =  self.current_pos[1] + next[i][1]

            if y >= 0 and x >=0 and y <= 7 and x <= 7:
                if self.knight_history[y][x] == 0:
                    possible.append(y)
                    possible.append(x)
                    final.append(possible)

        return final



#FUNCTIONS
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
        Worst Case: O(n) where n is the number of next moves returned
        Best Case: O(1) No next moves are available
    @parameter none
    @precondition The Tour class has been initialised
    @postcondition Displays a list of next possible legal moves, and
                    allow for user to move Knight to the position in list
    """
    try:
        next = board.next_moves()

        if len(next) > 0:
            for i in range(len(next)):
                print(str(i+1) + ". " + str(next[i]))

            user_move = int(input("Next move: ")) - 1
            if user_move >= 0 and user_move < len(next):
                posY = next[user_move][0]
                posX = next[user_move][1]
                board.move(posX,posY)
            else:
                raise IndexError

        else:
            print("There are no legal moves available.")

    except IndexError:
        print("Please choose from the valid positions above.")

    except ValueError:
        print("Please choose from the valid positions above.")

def menu():
    """
    @purpose To display the menu
    @complexity: O(1)
    @parameter None
    @precondition None
    @postcondition displays the menu and allows for user input
    """
    try:
        print("\n1. Quit")
        print("2. Start")
        print("3. Position")
        ans = int(input("Command: "))

        if ans == 1:
            print("User stopped the program.")
            global quit
            quit = True

        elif ans == 2:
            start()

        elif ans == 3:
            positions()

        else:
            raise ValueError

    except ValueError:
        print("Please input a valid command.")


if __name__ == "__main__":
    try:

        quit = False        #set flag
        board = Tour(0,1)   #initialise class Tour
        print("Welcome to Knight Tour. " +
              "\nPosition: [Rank y, File x]")
        while not quit:
            print("-"*30)
            board.display(8)
            menu()

    except KeyboardInterrupt:
        print("\nUser stopped the program.")