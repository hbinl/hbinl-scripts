__author__ = 'HaoBin'

def insertion_sort(list):
    """
    Complexity: Worst case O(N^2) when sorted backwards
        Best Case O(N) when sorted
    """
    for i in range(1,len(list)):
        tmp = list[i]
        j = i - 1
        while j >= 0 and list[j] > tmp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = tmp
    return list


if __name__ == "__main__":
    list = [2,92,0,2,1,5,10,1,4,2,5,1,0]
    list = insertion_sort(list)
    print(list)