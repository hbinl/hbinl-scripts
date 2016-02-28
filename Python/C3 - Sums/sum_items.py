"""
FIT1008 Prac 3 Task 1
@purpose Summing items in a list
@author Loh Hao Bin 25461257
@modified 20140809
@created 20140806
"""

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

def test_sum_items():
    """
    @purpose A function that calls sum_items with various test cases
    @param none
    @complexity O(1)
    """
    #some test cases
    list1 = [1, 2, 3, 4, 6] #valid numerical values
    print(sum_items(list1))
    list2 = range(0,10001)    #range of many values
    print(sum_items(list2))
    list3 = ["a",2,3]   #invalid values
    print(sum_items(list3))
    list4 = ["b"]       #invalid values
    print(sum_items(list4))
    list5 = [""]        #space
    print(sum_items(list5))
    list6 = []          #empty list
    print(sum_items(list6))
    list7 = [0.1,0.3,0.5,0.1]       #list with only real values
    print(sum_items(list7))

#MAIN
if __name__ == "__main__":
    test_sum_items()