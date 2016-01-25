__author__ = 'HaoBin'

import random

def partition_bootstrap(lst, k):
    # Generalised version of Dutch National Flag algorithm
    # k-way partitioning
    # First partitioning into three sub partitions,
    # then recursively partition the 3rd partition
    return partition(lst, list(range(k)))

def partition(lst,k):
    lo = 0
    mid = 0
    hi = len(lst)-1
    #print("k",k,"lst",lst)
    if len(k) >= 2:
        while mid <= hi:
            if lst[mid] == k[0]:
                lst[lo], lst[mid] = lst[mid], lst[lo]
                lo += 1
                mid += 1
            elif lst[mid] == k[1]:
                mid += 1
            elif lst[mid] in k[2:]:
                lst[mid], lst[hi] = lst[hi], lst[mid]
                hi -= 1
        #print(lst)
        l = []
        if len(k[2:]) > 1:
            l = partition(lst[hi+1:],k[2:])
            l = lst[0:hi+1] + l
        else:
            l = lst
        #print(">",l)
        return l
    else:
        #print(lst)
        return lst

def assertSorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True



def main():
    k = 200
    lst = []
    for i in range(10):
        lst.append(random.randrange(0,k))
    #lst = [1,2,1,2,2,3,0]
    #lst = [2,1,2,0,3,3,1]
    #lst = [0, 1, 0, 4, 3, 0, 0, 4, 2, 3]
    print(lst)
    lst = partition_bootstrap(lst,k)
    print(lst)
    sorted = assertSorted(lst)
    print("Sorted: " + str(sorted))


if __name__ == "__main__":
    main()