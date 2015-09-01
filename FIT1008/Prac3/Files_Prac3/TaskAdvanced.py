"""
FIT1008 Prac 3 - Advanced + Hall of Fame
@purpose Find Max Sum Interval of a list
@author Loh Hao Bin 25461257
@modified 20140809
@created 20140809
"""
import time, random

### Advanced Question ###########################################
def find_max_sum_interval(a_list):
    """
    Prac 3 Advanced Question
    @purpose Naively iterates through the list to find the max sum interval
    @param
        a_list: The list to be passed to find max sum interval indices
    @Complexity:
            O(N^3) - Worst Case: Two nested loops iterating through the whole list,
                                then inner loop in sum_items()
            O(1) - Best Case: When list is empty.
    @Precondition: An array of numerical values has to be passed
    @Postcondition: Returns the min and max indices for the max sum interval
    """
    i_min = 0
    i_max = 0
    maxSum = a_list[0]
    for min in range(0,len(a_list)):
        for max in range(min+1, len(a_list)+1):
            xsum = sum_items(a_list[min:max])
            if xsum > maxSum:
                maxSum = xsum
                i_max = max - 1
                i_min = min
    #print("Maximum sum is " + str(float(maxSum)))
    return i_min, i_max

def time_find_max_sum_interval(a_list):
    start = time.time()
    find_max_sum_interval(a_list)
    taken = time.time() - start
    return taken

### Hall of Fame ###########################################
def quick_find_max_sum_interval(a_list):
    """
    Prac 3 Hall of Fame
    @purpose variant of Kadane's Algorithm for maximum subarray problems,
        to find the max sum interval in this case, using dynamic programming
    @param
        a_list: The list to be passed to find max sum interval indices
    @Complexity:
            O(N) - Worst Case: Iterating through the list of N items
            O(1) - Best Case: Empty list
    @Precondition: An array of numerical values has to be passed
    @Postcondition: Returns the min and max indices for the max sum interval
    """
    currentMax = a_list[0]
    maxSum = a_list[0]
    i_min = i_min_tmp = 0
    i_max = 0
    for i in range(1, len(a_list)):
        if currentMax >= 0:
            currentMax += a_list[i]
        else:
            currentMax = a_list[i]
            i_min_tmp = i

        if maxSum <= currentMax:
            i_max = i
            i_min = i_min_tmp
            maxSum = currentMax
    #print("Maximum sum is " + str(float(maxSum)))
    return i_min, i_max

def time_quick_find_max_sum_interval(a_list):
    start = time.time()
    quick_find_max_sum_interval(a_list)
    taken = time.time() - start
    return taken

##################################################################
def sum_items(a_list):
    """
    @purpose Returns the sum of all items in a_list, and return 0 if empty list
    @param
        a_list: a list of items passed to this function to sum
    @complexity:
        Worst Case - O(N): When summing all values of a list with N items
        Best Case - O(1): when passing empty list
    @precondition Passing a list with numerical values
    @postcondition Return the sum of those numerical values in list
    """
    try:
        if len(a_list) > 0:
            #Naive linear iterating to sum
            sum = 0
            for i in range(len(a_list)):
                sum += a_list[i]
            return sum
        else:
            return 0
    except TypeError:
        return "Please only insert numerical type lists."

def test_time(a_list):
    """
    @purpose: A wrapper for the two functions to test and record their runtimes
    @param a_list: a list to be passed
    """
    print("find_max_sum_interval()")
    start = time.time()
    print("Index: " + str(find_max_sum_interval(a_list)))
    taken = format(time.time() - start, ".20f")
    print("Time taken: " + str(taken) + "s\n")

    print("quick_find_max_sum_interval()")
    start = time.time()
    print("Index: " + str(quick_find_max_sum_interval(a_list)))
    taken = format(time.time() - start, ".20f")
    print("Time taken: " + str(taken) + "s")

#MAIN  ###################################################
if __name__ == "__main__":
    try:
        a_list = []
        random.seed()
        for i in range(101):
           a_list.append(random.uniform(-1,1))

        for i in range(1,22):
            n = 2**i
            print(str(n) + " " + str(time_find_max_sum_interval(a_list[:n])))
        print("\n")
        for i in range(1,22):
            n = 2**i
            print(str(n) + " " + str(time_quick_find_max_sum_interval(a_list[:n])))

        #test_time(a_list)
    except:
        print("Error: Please input a numerical list.")
