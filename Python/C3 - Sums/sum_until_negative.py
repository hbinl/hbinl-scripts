"""
FIT1008 Prac 3 Task 3
@purpose Summing items until a negative number is reached, for Task 3
@author Loh Hao Bin 25461257
@modified 20140810
@created 20140807
"""
import time, random

def sum_until_negative(a_list):
    """
    @purpose Summing items in a list, stops as soon as a negative number is reached.
            If first item is negative, or list is empty, returns 0
    @parameter
        a_list: A list passed to be summed until negative number reached
    @Complexity:    Worst Case - O(N): goes through the whole list when none is negative
                    Best Case - O(1): empty list or first is negative
    @pre-condition An integer list is passed
    @post-condition Returns the sum of numbers up until negative number reached
    """
    try:
        sum = 0
        if len(a_list) > 0:
            for i in range(len(a_list)):
                if a_list[i] >= 0:
                    sum += a_list[i]
                else:   # if encountered a negative number, stop
                    return sum
            return sum
        else:
            return sum
    except TypeError:
        return "Please only insert numerical type lists."


def time_sum_until_negative(a_list):
    """
    @purpose Returns the time taken in seconds, for summing a list using sum_until_negative()
    @param
        a_list: a list of items passed to this function to be passed to sum_until_negative()
    @complexity: O(1)
    @precondition Passing a list
    @postcondition Return the time taken in seconds
    """
    start = time.time()
    total = sum_until_negative(a_list)
    taken = (time.time() - start)
    return taken

def table_time_sum_until_negative_1():
    """
    @purpose Generates a list of 1 million real values using random.seed() and random.uniform(),
            ranging from -1 to 1, then prints out: for each n, in steps of 2, up to 1 million,
            the time taken for summing from list[0] to list[n]
    @complexity:
        Worst Case: O(n log n) : when none of the item in list is negative.
        Best Case: O(log n): when the first item is negative. Because the algorithm always generate N items,
        then loop through log n items, then stop when it encounters the negative item.

    @postcondition Return a list of times
    """
    random_list = []    # initialising the list
    random.seed(1)
    while len(random_list) < 1500000:
        # Generates a million real values between -0.1 and 1
        random_list.append(random.uniform(-0.1,1))

    print("\n")
    n=1
    while n < len(random_list):
        print(str(n) + ", " + str(time_sum_until_negative(random_list[:n])))
        n = n*2

def table_time_sum_until_negative_2():
    """
    @purpose Generates a list of 1 million real values using random.seed() and random.uniform(),
            ranging from -1 to 1, then prints out: for each n, in steps of 2, up to 1 million,
            the time taken for summing from list[0] to list[n]
            This one also makes sure the first item is negative.
    @complexity:
        Best & Worst: O(log N): The algorithm always generate N items, then go through log n iteration,
                    but stops at first item everytime.
    @precondition none
    @postcondition Return a list of times
    """
    random_list = [-1]
    #random_list.append(random.uniform(-1,-0.001))  # Making sure first item is a negative
    random.seed(1)
    while len(random_list) < 1500000:
        random_list.append(random.uniform(-1,1))
    print("\n")
    n=1
    while n < len(random_list):
        print(str(n) + ", " + str(time_sum_until_negative(random_list[:n])))
        n = n*2

def test_sum_until_negative():
    """
    @purpose A function that calls sum_items with various test cases
    @param none
    @complexity O(1)
    """
    #some test cases
    list1 = [1, 2, 3, 4] #valid numerical values
    print(sum_until_negative(list1))
    list2 = []    #range of many values
    print(sum_until_negative(list2))
    list3 = [-1,2,3]   #invalid values
    print(sum_until_negative(list3))
    list4 = [1,3,-2,4]       #invalid values
    print(sum_until_negative(list4))
    list5 = ["a"]        #space
    print(sum_until_negative(list5))


#MAIN
if __name__ == "__main__":
    try:
        table_time_sum_until_negative_1()
        table_time_sum_until_negative_2()
        #test_sum_until_negative()

    except KeyboardInterrupt:
        print("Stopped by user.")