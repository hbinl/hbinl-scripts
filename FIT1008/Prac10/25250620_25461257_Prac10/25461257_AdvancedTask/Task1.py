"""
FIT1008 Prac 10 Task 1
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: I/O and interators
@created 20141009
@modified 20141009
"""

import random

def read_file(filename):
    '''
    @purpose: Read a file with filename specified, and return the object
    @complexity: O(1)
    @parameter: filename - name of the file to be read
    @precondition: A filename is passed
    @postcondition: Returns a file object
    '''
    file = open(filename, 'r')
    return file

def write_file(filename, content):
    '''
    @purpose: Write a file with filename specified
    @complexity: O(1)
    @parameter: filename - name of the file; content: the content to be saved
    @precondition: None
    @postcondition: returns 1 if the file is saved successfully, and creates a file
                    in the directory
    '''
    file = open(filename, 'w')
    file.write(content)
    file.close()
    return 1

def char_count(file):
    '''
    @purpose: To count the number of characters in the file
    @complexity: O(n) where n is the length of the file
    @parameter: file - the file object
    @precondition: A file object is passed
    @postcondition: Returns the character count
    '''
    file.seek(0)
    i = 0
    while file.read(1) != '':
        i += 1
    file.seek(0)
    return i

def convert_min(file):
    '''
    @purpose: Read characters in a file and make them lowercase
    @complexity: O(n) where n is the length of the file
    @parameter: file - the file object
    @precondition: A file object is passed
    @postcondition: Returns a string of converted characters
    '''
    file.seek(0)
    end = False
    output = ''
    while not end:
        c = file.read(1)
        if c == '':
            end = True
        else:
            if c.isalpha() == True:
                if c.isupper() == True:
                    output += c.lower()
                else:
                    output += c
    return output

def ask_convert_min():
    '''
    @purpose: Task 1 part (ii)
    @complexity: O(n) where n is the length of the file
    @parameter: None
    @precondition: None
    @postcondition: A file with converted lowercase characters is written
    '''
    filename = str(input("Input filename: "))
    o_filename = str(input("Output filename: "))
    file = read_file(filename)
    converted = convert_min(file)
    write_file(o_filename, converted)

def sort_count_dict():
    '''
    @purpose: Constructs a reference dictionary for alphabets
    @complexity: O(1)
    @parameter: None
    @precondition: None
    @postcondition: Returns a dictionary containing a-z
    '''
    str = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    for c in str:
        dict[c] = 0
    return dict

def sort_count(file = ''):
    '''
    @purpose: Task 1 part (iii)
    @complexity: O(n) where n is the length of the file
    @parameter: None
    @precondition: None
    @postcondition: Prints out characters in the file with their frequency
                    in descending order
    '''
    #reading file
    if file == '':
        filename = str(input("Input filename: "))
        file = read_file(filename)

    #constructing references
    ref_list = sort_count_dict()
    alphabets = list(ref_list.keys())

    #starting the loop to read file
    end = False
    while not end:
        c = file.read(1)
        if c in alphabets:
            # if alphabetical, increment frequency count
            ref_list[c] += 1
        elif c == '':
            end = True

    #construct a final list with all the alphabets with non-zero frequencies
    final_list = []
    for c in alphabets:
        if ref_list[c] != 0:
            final_list.append([c,ref_list[c]])

    # customised merge_sort it
    final_list = merge_sort(final_list)

    # print out the result
    for i in range(0, len(final_list)):
        print(str(final_list[i][0]) + ' : ' + str(final_list[i][1]))

    return final_list

def merge_sort(list):
    '''
    @purpose: Recursive merge sort starter, sorting into descending order
            Modified to work with list of lists, sorting based on the
            index 1 of each inner list.
    @complexity:
        O(n log n) where n is the length of the list
    @parameter: list - the list of list
    @precondition: A list of list is passed
    @postcondition: Returns a list of list sorted in descending order.
    '''
    tmp = [None] * len(list)
    start = 0
    end = len(list) - 1
    merge_sort_aux(list, start, end, tmp)
    return list

def merge_sort_aux(list, start, end, tmp):
    '''
    @purpose: Auxiliary function for recursive merge sort modified to fit task 1
    @complexity: O(log n) where n is length of outer list
    @parameter:
        List: the list to be sorted
        Start: The starting index of the splitted list
        End: The ending index of splitted list
        Tmp: A temporary list initialised for merging later
    @precondition:
    @postcondition:
    '''
    if start < end:
        mid = (start + end) // 2
        merge_sort_aux(list, start, mid, tmp)
        merge_sort_aux(list, mid+1, end, tmp)
        tmp = merge_arrays(list, start, mid, end, tmp)
        for i in range(start, end+1):
            list[i] = tmp[i]

def merge_arrays(a, start, mid, end, tmp):
    '''
    @purpose: Merge + sort
    @complexity: O(n) where n is the length of the list
    @parameter:
        a - the list
        start - starting index
        mid - the middle index
        end - the ending index
        tmp - a temporary list for swapping things
    @precondition: A list that has been segmented with start, mid, end indices
    @postcondition: Returns a single sorted list resulting from the
                    merging of two splitted lists
    '''
    ia = start
    ib = mid+1
    for k in range(start, end+1):
        if ia > mid: # a finished, copy b
           tmp[k] = a[ib]
           ib += 1
        elif ib > end: # b finished, copy a
           tmp[k] = a[ia]
           ia += 1
        elif a[ia][1] >= a[ib][1]: # a[ia] is the item to copy
           tmp[k] = a[ia]
           ia += 1
        else:
           tmp[k] = a[ib] # b[ib] is the item to copy
           ib += 1
    return tmp

def main():
    quit = False
    while not quit:
        try:
            print('\n1. Read and print how many characters')
            print('2. Take character, make lowercase, write')
            print('3. Character frequency count + merge sort')
            print('4. Quit')
            cmd = int(input(">> "))
            if cmd == 1:
                filename = str(input("Filename: "))
                file = read_file(filename)
                print(char_count(file))
            elif cmd == 2:
                ask_convert_min()
            elif cmd == 3:
                sort_count()
            elif cmd == 4:
                quit = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid command.")
        except FileNotFoundError:
            print("File not found.")


def test_t1_merge_sort():
    list = [['a',3],['b',1],['c',10],['k',7],['e',18]]
    merge_sort(list)
    print(list)


if __name__ == '__main__':
    try:
        test_t1_merge_sort()
        #main()
    except KeyboardInterrupt:
        pass
