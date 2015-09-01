__author__ = 'Ian Lim'


"""
The coming section is to provide additional information on Python's handling for List of List
"""


def test_list():
    print("======================================================")
    # building list of list
    current_list = []
    current_row_01 = [0, 1, 2]
    current_row_02 = []
    current_list.append(current_row_01)
    current_list.append(current_row_02)
    print(current_list)
    # notice below how modifying current_row_02 affects the current_list too. This is because current_list[1] actually references current_row[2]
    current_row_02.append(9)
    print(current_list)
    # a way around this is to use copy which assigns value instead of reference. As you can see below here, the third row is now unaffected by the 100 append
    current_list.append(current_row_02.copy())
    print(current_list)
    current_row_02.append(1000)
    print(current_list)
    # to access the 2nd list [index 1)
    print(current_list[1])
    # to access the 1st element (index 0) of the 2nd row (index 1) is to do the below
    print(current_list[1][0])
    print("======================================================")


test_list()