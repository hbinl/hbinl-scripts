"""
FIT1008 Prac 4 Task 2
@purpose Leap Year
@author Loh Hao Bin 25461257
@modified 20140815
@created 20140813
"""

def leap_year(y):
        """
        @purpose Returns whether the year is leap year or not
        @param y: the year to test for leap year
        @complexity:
            Best Case: O(2): When user input a year before 1582
            Worst Case: O(7): When user enter a year after 1582
        @precondition Passing a valid year in integer/numerical
        @postcondition Return whether the year is leap or not   
        """
        if y >= 1582:
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                return("Is a leap year")
            else:
                return("Is not a leap year")
        else:
            return("Please input a valid Gregorian calendar year after 1582.")

def test():
    print(leap_year(2014))
    print(leap_year(2012))
    print(leap_year(1900))
    print(leap_year(1400))
    print(leap_year("a"))

if __name__ == "__main__":
    try:
        test()
        #year = int(input("Please input a year: "))
        #print(leap_year(year))
    except:
        print("Please input a valid year in integer.")