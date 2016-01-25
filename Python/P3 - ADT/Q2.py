__author__ = 'HaoBin'

def binary_search_recursive(list, key, hi="", lo=0):
    if hi == "":
        hi = len(list) - 1
    if lo > hi:
        return -1
    else:
        mid = (lo + hi) // 2
        if key == list[mid]:
            return mid
        elif key > list[mid]:
            return binary_search_recursive(list, key, hi, mid+1)
        elif key < list[mid]:
            return binary_search_recursive(list, key, mid-1, 0)

def binary_search_iterative(list, key):
    hi = len(list) - 1
    lo = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if key == list[mid]:
            return mid
        elif key > list[mid]:
            lo = mid+1
        elif key < list[mid]:
            hi = mid-1
    return -2


if __name__ == "__main__":
    list = [0,1,2,3,4,5]
    key = int(input("Key? "))
    index = binary_search_iterative(list, key)
    print(index)
    index = binary_search_recursive(list, key)
    print(index)
