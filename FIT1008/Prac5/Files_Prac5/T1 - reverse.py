"""
FIT1008 Prac 5 Task 1
@purpose reverse.py
@author Loh Hao Bin 25461257, Derwinn Ee 25216384
@modified 20140823
@created 20140821
"""

def reverse():
    """
    @purpose: To read in a size n, then input a list of size n, then prints out
            in reverse order
    @param: none
    @complexity: O(N) where N is the size of input for list
    @precondition: A valid size is entered
    @postcondition: Prints out the list in reverse order
    """
    try:
        the_list = []
        i = 0
        size = 0
        size = int(input("Please input the size of the list: "))
        if size <= 0:
            print("Please input a valid length.")
        else:
            the_list = [0]*size
            while i < size:
                the_list[i] = (input("Item: "))
                i += 1
            i = size - 1
            while i >= 0:
                print(the_list[i], end=" ")
                i -= 1

    except:
        print("Please input a valid length.")

if __name__ == "__main__":
    reverse()