__author__ = 'HaoBin'

import random

def partition(lst):
    lo = 0
    mid = 0
    hi = len(lst)-1

    while mid <= hi:
        if lst[mid] == 0:
            lst[lo], lst[mid] = lst[mid], lst[lo]
            lo += 1
            mid += 1
        elif lst[mid] == 1:
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[hi] = lst[hi], lst[mid]
            hi -= 1
        print(lo,mid,hi,lst)


    return lst


def assertSorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def partitionAnalysis(lst):
    c0 = 0
    c1 = 0
    c2 = 0
    p1_flag = 0
    p2_flag = 0
    p3_flag = -1
    p4_flag = len(lst)
    for i in range(len(lst)):
        c = lst[i]
        if c == 0:
            c0 += 1
            p2_flag += 1
        elif c == 1:
            c1 += 1
            if p3_flag == -1:
                p3_flag = p2_flag + 1
            else:
                p3_flag += 1
        elif c == 2:
            c2 += 1

    print(c0, c1, c2)
    print(p1_flag,p2_flag,p3_flag,p4_flag)


def main():
    lst = []
    for i in range(10):
        lst.append(random.randrange(0,3))
    #print(lst)
    #lst = [0,0,0,1,1,1,2,2,2,2]
    lst = partition(lst)
    #print(lst)
    sorted = assertSorted(lst)
    print("Sorted: " + str(sorted))
    if sorted:
        partitionAnalysis(lst)

if __name__ == "__main__":
    main()