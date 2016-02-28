"""
Task 1
@purpose This program requests for a positive integer, and prints out all primes less than the specified integer.
@author Loh Hao Bin 25461257
@since 20140803
@modified 20140806
@complexity O(n^2)
@precondition: The user inputs a positive integer
@postcondition: Primes less than the input are printed out

Changes:
Line 17: original was (n=2), should be == comparison operator
Line 22,24,29: Boolean value True/False should be capitalised for first character, original was true/false
Line 23: n%2==1 should be n%2==0 in order to check for even numbers
Line 26: Instead of k*k<n, should be k<n
Line 20: Added a default flag=True assumption to catch errors about unassigned flag values, since if it's not 2, not even, not 1,
and not divisible by any integer up to sqrt(n), we can say that it's a prime number
Line 37: Added a check to see if integer is a positive number
"""
#import math

def is_prime(n):
    """
    @purpose Checks whether the passed number, n is prime, and return True/False
    @parameters: n - the number to be checked for primeness
    @complexity: O(n)
    @precondition: The function is passed a positive integer value
    @postcondition: Returns a true/false depending on primeness
    """
    k = 3
    flag = True
    if (n == 2):  #if it's 2, it's prime
        flag = True
    elif (n % 2 == 0 or n == 1):  #if even number or 1, then not prime
        flag = False
    else:
        while (k < n):
        #while (k <= math.sqrt(n)):  alternative, we only have to do trial divison on numbers up to sqrt(n)
            if (n % k == 0):
                flag = False
                break
            k += 1
    return flag


#MAIN BLOCK
try:
    n = int(input('Please enter a positive integer: '))   #request input from user

    if n >= 0:   #check if integer is positive
        for i in range(n):    #iterate from 0 to n
            if (is_prime(i)):    #if i is prime, print i
                print(i)
    else:
        print("The integer inputted is not positive.")

except ValueError:
    print("Invalid input.")

