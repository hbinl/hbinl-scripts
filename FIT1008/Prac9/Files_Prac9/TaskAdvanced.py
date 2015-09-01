"""
FIT1008 Prac 9 Advanced Task
Loh Hao Bin 25461257
@purpose: Text Editor COMMAND style - Extended
@created 20141002
@modified 20141003
"""

from Task1 import Node, LinkedList
from Task2 import *
from Task3 import *

def search(linked_list, keyword = ''):
    """
        @purpose: Look for lines with specific keyword
        @parameter: linked_list: The source
                    keyword: The word to be searched for
        @complexity: Best and Worst Case: O(n) where n is the length of the list
        @precondition: Linked list object initialised
        @postcondition: Prints out the matching lines, and returns the line numbers in list form
    """
    if keyword == '':
        print('?')
    else:
        results = []
        for i in range(len(linked_list)):
            line = linked_list.return_content(i)
            if line.find(keyword) != -1:
                print('Line ' + str(i) + ': ' + str(line))
                results.append(i)
        print('Found ' + str(len(results)) + ' lines.')
        return results



def replace(linked_list, param = ''):
    """
        @purpose: Find and replace a specific keyword
        @parameter: linked_list: The source
                    param: The unsplitted parameter given by user
        @complexity: O(n) where n is the length of the list
        @precondition: Linked list object initialised
        @postcondition: Replaces all instances of the keyword with new_word
    """
    # splits the parameter by single quotes
    s_param = param.split('\' \'', 1)

    #first word
    word = s_param[0][1:len(s_param[0])]
    #get second word
    new_word = s_param[1][0:len(s_param[1])-1]

    print("Replacing...")

    '''
    # Alternative less efficient way
    results = search(linked_list, word)
    for ln in results:
        line = linked_list.return_content(ln)
        #print(line)
        line = line.replace(word, new_word)
        print('Line ' + str(ln) + ': ' + line)
        linked_list.delete(ln)
        linked_list.insert(ln, line)
    '''

    #loop through the whole list
    n = 0
    for i in range(len(linked_list)):
        # get the current line at i
        line = linked_list.return_content(i)
        # look for keyword
        if line.find(word) != -1:
            # if found something
            print('Line ' + str(i) + ': ' + str(line))
            # replace it
            line = line.replace(word, new_word)
            print('->' + str(line))
            # delete and reinsert
            linked_list.delete(i)
            linked_list.insert(i, line)
            n += 1

    print('Replaced ' + str(n) + ' lines.')
    return linked_list

def ed_cmd2():
    # enhanced version's command menus
    print("Text File Only. v1+")
    print("Type 'h' for a list of available commands.")
    quit = False
    linked_list = LinkedList()
    while not quit:
        try:
            cmd = input("\n> ")

            if cmd == 'q':
                #quit
                quit = True

            elif cmd == 'h':
                # display help and list of commands
                print("List of commands available:\n" +
                      "r [filename] - Opens a file and read its contents\n"
                      "w [filename] - Writes memory into a file\n" +
                      "p [num] - Prints line [num] or [n:m]\n"+
                      "d [num] - Deletes line [num] or [n:m]\n" +
                      "q - quits the program\n" +
                      "i [num] - Insert at line [num]\n" +
                      "a - Append line\n" +
                      "n - Closes current file and starts new session\n" +
                      "g [keyword] - Finds the keyword, case sensitive\n" +
                      "s [word] [new_word] - Replace [word] with [new_word], enclose parameters in single quotation")
            else:
                # else, interpret and split the command
                params = cmd.split(' ', 1)
                #
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

                        if params[1].find(':') == -1:
                            num = params[1]
                            print_line(linked_list, num)

                        else:
                            # HOF: range print
                            p = params[1].split(':')
                            start = int(p[0])
                            end = int(p[1])
                            if start <= end:
                                for i in range(start,end):
                                    print_line(linked_list, i)

                            else:
                                raise IndexError

                    else:
                        # if no parameter given
                        print_line(linked_list, '')

                elif params[0] == 'd':

                    # delete line
                    if len(params) == 2:
                        if params[1].find(':') == -1:
                            num = params[1]
                            delete_line(linked_list, num)
                        else:
                            #HOF: range delete
                            p = params[1].split(':')
                            start = int(p[0])
                            end = int(p[1])
                            if start <= end:
                                for _ in range(end-start):
                                    delete_line(linked_list, start)
                                    print('delete')
                            else:
                                raise IndexError
                    else:
                        # if no parameter given
                        delete_line(linked_list, '')

                elif params[0] == 'i':
                    # insert line
                    num = params[1]
                    insert_text(num, linked_list)

                elif params[0] == 'a':
                    # append line
                    num = len(linked_list) + 1
                    insert_text(num, linked_list)

                elif params[0] == 'g':

                    #find a certain word
                    keyword = params[1]
                    results = search(linked_list, keyword)

                elif params[0] == 's':
                    # search and replace
                    linked_list = replace(linked_list, params[1])

                elif params[0] == 'n':
                    # hidden___: new file
                    linked_list = LinkedList()

                elif params[0] == 'test':
                    # calls the test function
                    ed_cmd2_test()
                    quit = True

                elif params[0] == '.':
                    # print how many lines lol
                    print(str(len(linked_list)) + ' Lines.')


                else:
                    # if unlike anything else
                    raise ValueError

        except ValueError:
            print("?")
        except AttributeError:
            print("?")
        except IndexError:
            print("?")

def ed_cmd2_test():
        x = LinkedList()
        x = read('tline.txt', x)
        print_line(x, '')

        print('\n> Testing g function')
        print('\nKeyword: is')
        search(x, 'is')
        print('\nKeyword: 5')
        search(x, '5')
        print('\nKeyword: empty')
        search(x, '')


        print('> Testing s function')
        print('s \' is\' \' was\'')
        replace(x, '\' is\' \' was\'')

        print('s with empty')
        replace(x, '')

if __name__ == "__main__":
    try:
        #Text File Only.
        ed_cmd2()
    except KeyboardInterrupt:
        print()