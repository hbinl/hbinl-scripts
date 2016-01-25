"""
FIT1008 Prac 5 Task 2
@purpose binary.py
@author Loh Hao Bin 25461257, Derwinn Ee 25216384
@modified 20140823
@created 20140822
"""

def binary():
    """
    @purpose This function accepts a positive integer,
            and outputs the binary representation of the integer.
    @parameter: None
    @complexity:
        Best Case: O(1) - When the integer input is not positive
        Worst Case: O(log n)
            where n is the number of user input
    @precondition: A positive integer value is passed
    @postcondition: Prints the binary value of the integer n
    """
    try:
        n = int(input("Please input a positive integer: "))
        if n > 0:
            rev_binary = [0] * n

            length = 0
            while n > 0:
                rev_binary[length] = int(n%2)
                n = int((n - n%2) / 2)
                length += 1
            rev_binary = rev_binary[0:length]
            length -= 1
            while length >= 0:
                print(rev_binary[length], end="")
                length -= 1

        else:
            print("Please enter a valid positive integer greater than zero.")
    except:
        print("Please enter a valid positive integer greater than zero.")


if __name__ == "__main__":
    binary()
