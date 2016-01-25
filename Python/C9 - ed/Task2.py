"""
FIT1008 Prac 9 Task 2
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: Text Editor MENU style
@created 20141002
@modified 20141003
"""

from Task1 import Node, LinkedList

def read(filename, linked_list):
    """
        @purpose: Read the content of a file
        @parameter: filename: The filename of the file to be read
                    linked_list: A linked list as the destination for the file contents
        @complexity: Best Case: O(1): File does not exist
                     Worst Case: O(n): where n is the number of lines of the file
        @precondition: Linked list object initialised
        @postcondition: Returns a linked list with contents separated by lines
    """
    file = open(filename, 'r')
    print(">>>Reading " + filename + '...')
    for line in file:
        linked_list.append(line)
    linked_list.append('\n')
    print(filename + " opened.")
    file.close()

    return linked_list

def write(filename, linked_list):
    """
        @purpose: Write the content of linked list to file
        @parameter: filename: The filename to save as
                    linked_list: A linked list as the source of file contents
        @complexity: Best & Worst: O(n) where n is the length of linked list
        @precondition: Linked list object initialised
        @postcondition: A file [filename] is created with contents of the linked list
    """
    file = open(filename, 'w')
    print(">>>Writing " + filename + '...')
    file.write(linked_list.return_content())
    print(filename + " written to file.")
    file.close()

def print_line(linked_list, index = ''):
    """
        @purpose: Print a specified line
        @parameter: linked_list: The source
                    index (optional): The index of the list to be read
                                        else, it will print all lines
        @complexity: Best Case: O(1) - List is empty
                     Worst Case: O(n) - where n is length of the list
        @precondition: Linked list object initialised
        @postcondition: Prints out the line requested
    """
    print()
    if linked_list.is_empty() == True:
        raise IndexError

    if index == '':
        print(linked_list.return_content())
        print('>>> [' + str(len(linked_list)) + ' lines printed.]')
    else:
        index = int(index)
        if index >= 0:
            print(linked_list.return_content(index))
        else:
            index = len(linked_list) + index
            print(linked_list.return_content(index))
    #print('-' *60)


def delete_line(linked_list, index = ''):
    """
        @purpose: Delete a specified line
        @parameter: linked_list: The source
                    index (optional): The index of the list to be read
                                        else, it will delete all lines
        @complexity: Best Case: O(1) - Delete everything
                     Worst Case: O(n) where n is the index
        @precondition: Linked list object initialised
        @postcondition: Deletes the line requested
    """
    if index == '':
        linked_list.delete()
    else:
        index = int(index)
        if index >= 0:
            linked_list.delete(index)
        else:
            index = len(linked_list) + index
            linked_list.delete(index)

def ed_menu():
    # The menu for testing out the functions
    print("Text file only.")
    quit = False
    linked_list = LinkedList()
    while not quit:
        try:
            print("\n1. read [filename]")
            print("2. write [filename]")
            print("3. print [num]")
            print("4. delete [num]")
            print("5. Quit")
            print("6. Test Function")
            cmd = int(input("> "))

            if cmd == 1:
                #Read
                r_filename = str(input("Read Filename: "))
                if r_filename == '':
                    raise ValueError
                else:
                    linked_list = LinkedList()
                    linked_list = read(r_filename, linked_list)

            elif cmd == 2:
                #Write
                w_filename = str(input("Write Filename: "))
                write(w_filename, linked_list)

            elif cmd == 3:
                #Print
                if linked_list.is_empty() == False:
                    num = input("Print line number [blank for all]:")
                    print_line(linked_list, num)
                else:
                    raise IndexError

            elif cmd == 4:
                #Delete
                if linked_list.is_empty() == False:
                    num = input("Delete line number [blank for all]:")
                    delete_line(linked_list, num)
                else:
                    raise IndexError

            elif cmd == 5:
                #Quit
                quit = True

            elif cmd == 6:
                #Test Function
                t2_test()
                quit = True

            else:
                #invalid input
                raise ValueError

        except ValueError:
            print("?")
        except IndexError:
            print("?")
        except FileNotFoundError:
            print("?")

### TEST FUNCTIONS
def t2_test():
    print("="*30)
    try:
        print("> Test Read File: TEXT1.txt and inexistent file 4.txt")
        test_read()
    except FileNotFoundError:
        print("?")
    print("="*30)
    print("> Test Write File named XXXXX.txt with contents 1,2,3,4")
    test_write()
    print("="*30)
    print("Test Delete line on Text1.txt")
    test_delete_line()

def test_read():
        # TEST READING FILE
        x = LinkedList()
        x = read('TEXT1.txt', x)
        print_line(x)
        x = read('4.txt', x)
        print_line(x)


def test_write():
        # TEST WRITING FILE
        x = LinkedList()
        x.append('1\n')
        x.append('2\n')
        x.append('3\n')
        x.append('4\n')
        write('XXXXX.txt', x)


def test_delete_line():
        # TEST DELETING THINGS
        x = LinkedList()
        x = read('TEXT1.txt', x)
        print("\n>>>Printing line 3")
        print_line(x, 3)

        #print("\n>>>Printing everything")
        #print_line(x)

        print("\n>>>Deleting line 3")
        delete_line(x, 3)
        print("Line 3 is now:")
        print_line(x,3)

        try:
            print("\n>>>Deleting line a")
            delete_line(x, 'a')
            print_line(x)
        except ValueError:
            print("?")

        write('Y.txt',x)

        print("\n>>>Deleting everything")
        delete_line(x, '')
        print_line(x, '')
        write('Z.txt',x)


if __name__ == "__main__":
    try:
        ed_menu()
    except KeyboardInterrupt:
        print()