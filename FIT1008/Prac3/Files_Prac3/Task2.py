"""
FIT1008 Prac 3 Task 2
@purpose Summing items in a random generated list with 1 million items, from Task 2
@author Loh Hao Bin 25461257
@modified 20140810
@created 20140807
@complexity O(N^2)
"""
import random, time

def sum_items(a_list):
    """
    @purpose Returns the sum of all items in a_list, and return 0 if empty list
    @param
        a_list: a list of items passed to this function to sum
    @complexity:
        Worst Case - O(N): When summing all values of a list with N items
        Best Case - O(1): when passing empty list or encounter error
    @precondition Passing a list with numerical values
    @postcondition Return the sum of those numerical values in list, or 0 if it's empty
    """
    try:
        if len(a_list) > 0:
            sum = 0
            for i in range(len(a_list)):
                sum += a_list[i]
            return sum
        else:
            return 0
    except TypeError:
        return "Please only insert numerical type lists."


def time_sum_items(a_list):
    """
    @purpose Returns the time taken in seconds, for summing a list using sum_items() function
    @param
        a_list: a list of items passed to this function to be passed to sum_items()
    @complexity:
        Best Case: O(1): when passing a list that is empty
        Worst Case: O(N): when passing a list to be summed of all values
    @precondition Passing a list
    @postcondition Return the time taken in seconds
    """
    start = time.time()
    sumx = sum_items(a_list)
    taken = (time.time() - start)
    return taken

def table_time_sum_items():
    """
    @purpose Generates a list of 1 million real values using random.seed() and random.random(),
        then prints out: for each n, in steps of 2, up to 1 million, the time taken for summing from
        list[0] to list[n]
    @complexity:
        Best Case: O(log n): When the list is generated, then go through log n iterations
        Worst Case: O(N log n): When the algorithm loops through log n iteration and sums up n items.
    @precondition none
    @postcondition Return a list of times
    """
    random_list = []
    random.seed(1)
    while len(random_list) < 1500000:
        random_list.append(random.random())


    print("\n")
    n=1
    while n < len(random_list):
        print(str(n) + ", " + str(time_sum_items(random_list[:n])))
        n = n * 2

#MAIN
if __name__ == "__main__":
    try:
        table_time_sum_items()

    except KeyboardInterrupt:
        print("Stopped by user.")