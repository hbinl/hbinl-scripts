"""
FIT1008 Prac 9 Task 3
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: Text Editor COMMAND style
@created 20141002
@modified 20141003
"""

from Task1 import Node, LinkedList
from Task2 import *

def insert_text(num, linked_list):
    """
        @purpose: Insert text mode
        @parameter: linked_list: The source
                    num: The line number to insert the text at
        @complexity: Best Case: O(1) when num is invalid
                     Worst Case: O(n) where n is length of user input
        @precondition: Linked list object initialised
        @postcondition: Insert the text inputted at the line specified
    """
    num = int(num)
    enter_mode = True

    # if index is positive
    if num >= 0:
        num = int(num)

        #start input mode
        while enter_mode:
            txt = str(input())
            #check if period on single line
            if txt == '.':
                enter_mode = False
            else:
                #append with line break and go to next line
                txt = txt + '\n'
                linked_list.insert(num, txt)
                #increment num for next line
                num += 1
    else:
        #if index is negative, wrap around
        num = len(linked_list) + num
        while enter_mode:
            txt = str(input())
            if txt == '.':
                enter_mode = False
            else:
                txt = txt + '\n'
                linked_list.insert(num, txt)
                num += 1

def ed_cmd():
    #cmd menu

    print("Text file only. v1")
    print("Type 'h' for a list of available commands.")
    quit = False

    #initialise linked list
    linked_list = LinkedList()
    while not quit:
        try:
            cmd = input("\n> ")
            #accept user input

            if cmd == 'q':
                # quit
                quit = True

            elif cmd == 'h':
                # help and list of commands
                print("List of commands available:" )
                print("r [filename] - Opens a file and read its contents")
                print("w [filename] - Writes memory into a file")
                print("p [num]      - Prints line [num]")
                print("d [num]      - Deletes line [num]")
                print("i [num]      - Insert at line [num]")
                print("a            - Append line")
                print("q            - quits the program")
            else:
                # interpreting the command by splitting the command and parameters
                params = cmd.split(' ', 1)

                # if command is...
                if params[0] == 'r':
                    # read file
                    filename = params[1]
                    linked_list = LinkedList()
                    read(filename, linked_list)

                elif params[0] == 'w':
                    # write file
                    filename = params[1]
                    write(filename, linked_list)

                elif params[0] == 'p':
                    # print line
                    if len(params) == 2:
                        # if line_number parameter given
                        num = params[1]
                        print_line(linked_list, num)
                    else:
                        # if no parameter given or too many parameters
                        print_line(linked_list, '')

                elif params[0] == 'd':
                    # delete line
                    if len(params) == 2:
                        # if line number parameter given
                        num = params[1]
                        delete_line(linked_list, num)
                    else:
                        #if no parameter given
                        delete_line(linked_list, '')

                elif params[0] == 'i':
                    # insert line
                    num = params[1]
                    insert_text(num, linked_list)

                elif params[0] == 'a':
                    if len(params) == 1:
                        # append line
                        num = len(linked_list) + 1
                        insert_text(num, linked_list)
                    else:
                        raise ValueError

                elif params[0] == 'test':
                    # calls the test function
                    ed_test()
                    quit = True
                else:
                    # if it's not like anything else
                    raise ValueError

        except ValueError:
            print("?")
        except FileNotFoundError:
            print("?")
        except IndexError:
            print("?")


### TEST CASE FUNCTIONS
def ed_test():
    print("="*30)
    print(">> Test Inserting things")
    test_insert()
    print("="*30)
    print("\n>> Test Appending things")
    test_a()


def test_insert():
        # Test insert function
        x = LinkedList()
        x = read('tline.txt', x)
        print_line(x, '')
        print(">>> Testing insert() or i [num] at line 3")
        print(">>> Start typing, and end with . on single line")
        insert_text(3, x)
        print(">>> Printing")
        print_line(x, '')

        try:
            print(">>> Insert at invalid index a")
            insert_text('a', x)
        except ValueError:
            print("?")

def test_a():
    # Test append function
    x = LinkedList()
    x = read('tline.txt', x)
    print(">>> Testing command a")
    print(">>> Your inserted text should appear last")
    num = len(x) + 1
    insert_text(num, x)
    print_line(x, '')


if __name__ == "__main__":
    try:
        ed_cmd()
    except KeyboardInterrupt:
        print()