"""
FIT1008 Prac 6 Task 1
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: Knight in Chess
            File: The columns
            Rank: The rows
@created 20140831
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
        @parameter none
        @precondition The Tour class has been initialised
        @postcondition prints out the current board state
        """
        print('')
        for i in range(n):
            for j in range(n):
                if (self.board[i][j] == 1) and (self.knight_history[i][j] == 1):
                    print("K", end=" ")
                elif self.knight_history[i][j] == 1 and (self.board[i][j] == 0):
                    print("*", end=" ")
                else:
                    print("0", end=" ")
            print('')


    def move(self,x,y):
        """
        @purpose To display the current chess board state
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
                self.knight_history[y][x] = 1
        else:
            #throw a ValueError to ask for valid x/y
            raise ValueError


#FUNCTIONS
def menu():
    """
    @purpose To display the menu
    @complexity: O(1)
    @parameter None
    @precondition None
    @postcondition displays the menu and allows for user input
    """
    try:

        print("\n1. Position")
        print("2. Quit")
        ans = int(input("Command: "))
        if ans == 1:

            try:

                posX = int(input("X (File): "))
                posY = int(input("Y (Rank): "))
                board.move(posX,posY)

            except ValueError:
                print("Please input a valid File and Rank.")

        elif ans == 2:

            #if Quit
            print("User stopped the program.")
            global quit
            quit = True

        else:
            #throw error to ask for valid command
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
