"""
FIT1008 Prac 4 Task 1
@purpose Pythagorian Triple
@author Loh Hao Bin 25461257
@modified 20140815
@created 20140813
"""
def absolute(n):
    """
    @purpose Returns the absolute value of n
    @param n: the value to return an abs value on
    @complexity:
        Best Case & Worst Case: O(1)
    @precondition Passing a valid integer value
    @postcondition Return the absolute value
    """
    if n <= 0:
        return n * -1
    else:
        return n

def pythagorian_triple(m,n):
    """
    @purpose Returns the Pythagorean Triple
    @param m,n: Integers to calculate Pythagorean Triple
    @complexity:
        Best Case: O(1) - When the input is not positive
        Worst Case: O(1) - When the input is valid
    @precondition Passing two valid integer values
    @postcondition Return the Pythagorean Triple
    """
    if m >= 0 and n >= 0:
        a = absolute(m**2 - n**2)
        b = 2*m*n
        c = m**2 + n**2
        return a, b, c
    else:
        return "Please input positive integers.", "Please input positive integers.", "Please input positive integers."


#MAIN
if __name__ == "__main__":
    try:
        #Requesting for input
        input1 = int(input("Please insert the first positive integer: "))
        input2 = int(input("Please insert the second positive integer: "))

        result = pythagorian_triple(input1,input2)
        #Printing a,b,c from returned tuple
        print("a = " + str(result[0]))
        print("b = " + str(result[1]))
        print("c = " + str(result[2]))

    except:
        print("Please input only integers.")
