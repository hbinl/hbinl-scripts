"""
FIT1008 Prac 5 Task 3
@purpose new_power.py
@author Loh Hao Bin 25461257, Derwinn Ee 25216384
@modified 20140825
@created 20140823
"""

def binary(e):
    """
    @purpose: Returns a binary representation of the integer passed
    @parameter: e - The integer to be converted to binary
    @precondition: A positive integer value is passed
    @postcondition: A list of integers representing binary value of the integer,
    @Complexity:
        Best Case: O(1) if e is 0
        Worst Case: O(e + log e) because the algorithm cuts e into half in the second loop
    """
    if e > 0:
        rev_binary = [0] * e

        length = 0
        while e > 0:
            rev_binary[length] = int(e%2)
            e = int((e - e%2) / 2)
            length += 1

        return rev_binary[0:length]
    else:
        return [0]

def power(b, e):
    """
    @purpose: Using a binary list to calculate power of two integers
    @param:
        b: The base number
        e: The exponent
    @precondition: A valid positive base and exponent are input
    @postcondition: The power of b^e is print out
    @Complexity:
        Best Case: O(1) if exponent < 0
        Worst Case: O(  )
    """


    if e < 0:
        return "Please input positive exponents"
    else:
        rev_binary = binary(e)
        result = 1
        idx = len(rev_binary) - 1
        while idx >= 0:
            result = result * result

            if rev_binary[idx]:
                result = result * b
            idx -= 1
        return result


if __name__ == "__main__":
    try:
        b = int(input("Please input a positive integer: "))
        e = int(input("Please input a positive integer: "))
        print(power(b,e))
    except:
        print("Please input a valid positive integer.")