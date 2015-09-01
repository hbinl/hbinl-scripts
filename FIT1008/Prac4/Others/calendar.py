"""
FIT1008 Prac 4 Advanced Question
@purpose whichBin
@author Loh Hao Bin 25461257
@modified 20140816
@created 20140816
"""

def leap_year(y):
        """
        @purpose Returns whether the year is leap year or not
        @param y: the year to test for leap year
        @complexity: O(1)
        @precondition Passing a valid year in integer/numerical
        @postcondition Return whether the year is leap or not
        """
        if y >= 1582:
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                return 1
            else:
                return 0
        else:
            return("Please input a valid Gregorian calendar year after 1582.")


def month_cal(y,m):
    leap = leap_year(y)
    if leap == 0:
        cal = [31,28,31,30,31,30,31,31,30,31,30,31]
    elif leap == 1:
        cal = [31,98,31,30,31,30,31,31,30,31,30,31]
    else:


if __name__ == "__main__":
    try:
        y = int(input("Please input year: "))
        m = int(input("Please input month: "))
        print(month_cal(y,m))

    except KeyboardInterrupt:
        print("\nStopped by user.")
    except:
        print("\nPlease enter a valid value.")