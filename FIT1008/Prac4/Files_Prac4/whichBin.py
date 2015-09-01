"""
FIT1008 Prac 4 Advanced Question
@purpose whichBin
@author Loh Hao Bin 25461257
@modified 20140816
@created 20140814
"""
def whichBin(d,m):
    """
    @purpose This algorithm which color bin you should put out on next Monday, in 2014.
    @complexity:
        Best Case: O(1) - When the date input is not valid
        Worst Case: O(N) - When month M get inputted
    @param: d - date; m - month
    @precondition: The function is passed a valid month and date in 2014.
    @postcondition: Returns the color of the bin for next Monday.
    """
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m <= 12 and m >= 1:
        if d >= 1 and d <= months[m-1]:
            sum_day = 0
            for i in range(m-1):
                sum_day += months[i]
            sum_day += d
            day = sum_day - 1   #Get the current day number,
            #print(day)                        #compensated for Monday such that Monday begins the week
            day_day = (day + 2) % 7 #Get the current date's weekday, +2 is to compensate for start of the year

            week_num = int( (day) / 7 + 1 ) #Get the current week number, then round down
            week_num += 1   #add a week for NEXT WEEK
            #print(week_num)
            first_day = 3 - 1   #Get the first day of the year's weekday
            if day_day < first_day:     #compensate for first weekday of the year
                week_num += 1

            #since 10th of March is an odd numbered week and yellow bin is put out
            #and we put our different colored bins alternatively in alternative weeks
            #we can say that even number week = green, odd = yellow
            if week_num % 2 == 0:
                return("Next Monday you should put out GREEN bin.")
            else:
                return("Next Monday you should put out YELLOW bin.")
        else:
            return("Please input a valid day.")
    else:
        return("Please input a valid month.")


if __name__ == "__main__":
    try:
        m = int(input("Please input month: "))
        d = int(input("Please input day: "))
        print(whichBin(d,m))
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except:
        print("\nPlease enter a valid value.")