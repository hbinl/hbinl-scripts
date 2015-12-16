'''
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified: 20141015
'''
alphabets = [['a',0], ['b',0], ['c',0], ['d',0], ['e',0], ['f',0], ['g',0], ['h',0], ['i',0], ['j',0], ['k',0], ['l',0], ['m',0], ['n',0], ['o',0], ['p',0], ['q',0], ['r',0], ['s',0], ['t',0], ['u',0], ['v',0], ['w',0], ['x',0], ['y',0], ['z',0]]

def main():
    inputfile = input('Enter the file name to be read: ')
    read(inputfile)

def read(inputfile):
    '''
    @precondition: A valid file
    @postcondition: none

    @param: inputfile

    @complexity:
    Best case: O(1) where the file does not exist
    Worst case: O(M + N log N) where M is the number of characters in the input file and N is the number of items at each level
    '''
    global alphabets
    alphabets = [['a',0], ['b',0], ['c',0], ['d',0], ['e',0], ['f',0], ['g',0], ['h',0], ['i',0], ['j',0], ['k',0], ['l',0], ['m',0], ['n',0], ['o',0], ['p',0], ['q',0], ['r',0], ['s',0], ['t',0], ['u',0], ['v',0], ['w',0], ['x',0], ['y',0], ['z',0]]
    try:
        reading = open(inputfile, 'r')
        read = reading.read()
        for i in read:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                change_count(i)
        merge_sort(alphabets)
        for j in alphabets:
            print(j)
    except:
        print('Error. Please enter a valid file to read.')

def change_count(i):
    '''
    @precondition: current alphabet
    @postcondition: alphabet count increased by 1

    @param: i

    @complexity: O(1)
    '''
    index = ord(i) - 97
    alphabets[index][1] += 1
    
def merge_sort(array):
    '''
    @precondition: an array of items
    @postcondition: a sorted array of items according to its frequency

    @param: array

    @complexity: O(N log N) where N is the number of items at each level
    '''
    tmp = [None] * len(array)
    start = 0
    end = len(array) - 1
    merge_sort_aux(array, start, end, tmp)

def merge_sort_aux(array, start, end, tmp):
    '''
    @precondition: an array of items
    @postcondition: a sorted array of items according to its frequency

    @param: array, start, end, tmp

    @complexity: O(N log N) where N is the number of items at each level
    '''
    if start < end:
        mid = (start+end) // 2
        merge_sort_aux(array, start, mid, tmp)
        merge_sort_aux(array, mid+1, end, tmp)
        merge_arrays(array, start, mid, end, tmp)
        for i in range(start, end+1):
            array[i] = tmp[i]

def merge_arrays(a, start, mid, end, tmp):
    '''
    @precondition: an array of items
    @postcondition: a sorted array of items according to its frequency

    @param: a, start, mid, end, tmp

    @complexity: O(N log N) where N is the number of items at each level
    '''
    ia = start
    ib = mid+1
    for k in range(start, end+1):
        if ia > mid:
            tmp[k] = a[ib]
            ib += 1
        elif ib > end:
            tmp[k] = a[ia]
            ia += 1
        elif a[ia][1] >= a[ib][1]:
            tmp[k] = a[ia]
            ia += 1
        else:
            tmp[k] = a[ib]
            ib += 1

if __name__ == "__main__":
    main()

#Test functions

def test_read():
    global alphabets
    alphabets = [['a',0], ['b',0], ['c',0], ['d',0], ['e',0], ['f',0], ['g',0], ['h',0], ['i',0], ['j',0], ['k',0], ['l',0], ['m',0], ['n',0], ['o',0], ['p',0], ['q',0], ['r',0], ['s',0], ['t',0], ['u',0], ['v',0], ['w',0], ['x',0], ['y',0], ['z',0]]
    print('\nTesting for counting characters in an empty file.')
    read('Empty.txt')
    print('Test success.')
    print('Testing for counting characters in a valid file.')
    read('Random.txt')
    print('Test success.')
    print('\nTesting for counting characters in a non-existant file.')
    read('No.txt')
    print('Test success.')

def test_change_count():
    global alphabets
    alphabets = [['a',0], ['b',0], ['c',0], ['d',0], ['e',0], ['f',0], ['g',0], ['h',0], ['i',0], ['j',0], ['k',0], ['l',0], ['m',0], ['n',0], ['o',0], ['p',0], ['q',0], ['r',0], ['s',0], ['t',0], ['u',0], ['v',0], ['w',0], ['x',0], ['y',0], ['z',0]]
    print('Testing for increasing frequency of alphabet a by 1.')
    change_count('a')
    print(alphabets)
    print('Test success.')
    print('\nTesting for increasing frequency of a non-alphabet @')
    try:
        change_count('@')
    except:
        print('Error. Please enter an alphabet.')
    print('Test success.')

def test_merge_sort():
    print('Testing for sorting an unsorted array of [[a, 4], [s, 1], [d, 3], [f, 2]].')
    list1 = [['a', '4'], ['s', '1'], ['d', '3'], ['f', '2']]
    merge_sort(list1)
    for i in list1:
        print(i)
    print('Test success.')
    print('\nTesting for sorting a sorted array [[q, 4], [w, 3], [e, 2], [r, 1]].')
    list2 = [['q', '4'], ['w', '3'], ['e', '2'], ['r', '1']]
    merge_sort(list2)
    for i in list2:
        print(i)
    print('Test success.')

