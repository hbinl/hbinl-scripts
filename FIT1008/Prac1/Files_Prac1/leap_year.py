"""
Accepts a year value from the user and output whether is the
year a leap year or not.

@author Hao Bin
@since 20140730
@modified 20140730
@param none
@precondition: User input an integer
@postcondition:  Output whether the year is a leap year or not
@complexity O(1)
"""

year = int(input('Enter year: '))
#Accept input from user

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    #Check if the year is divisible by 4 and not divisible by 100 or divisible by 400
    print(year, 'is a leap year')
else:
    print(year, 'is NOT a leap year')
