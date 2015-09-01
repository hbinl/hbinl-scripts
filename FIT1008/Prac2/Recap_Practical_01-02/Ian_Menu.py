__author__ = 'Ian Lim'


"""
A sample module based on Practical 02, Task 02 to demonstrate Python better.
The first section is on handling List, a data structure you'll be using a lot in Python for your units.
Note: Everything here is done simple
:author:    Ian Lim
:since:     20140805
:modified:  20140810
"""


def print_menu():
    """
    Prints the menu for the user
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :return: None
    :precondition: None
    :postconidtion: Prints out the menu
    :complexity: O(1)
    """
    print("-----------------")
    print("Menu:")
    print("1. append")
    print("2. sort")
    print("3. print")
    print("4. quit")
    print("5. clear")
    print("6. reverse")
    print("7. pop")
    print("8. size")
    print("9. insert")
    print("10. find")


def input_integer(new_message):
    """
    Prompts the user to enter an integer input and returns it
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_message: The message to be prompted to the user
    :return: User's integer input
    :precondition: None
    :postconidtion: A valid integer is entered by the user
    :complexity time: O(N)  where   N = Number of user inputs until an integer is entered
    """
    # loops till the user enter a valid integer
    while True:
        try:
            # the int() is casting the input to integer. the same concept for str()
            return int(input(new_message))
        # example of a known exception handling
        except ValueError:
            print("Invalid input: Please enter an Integer.")
        # maybe other type of exceptions?
        except:
            print("Some Error which I dunno lol")


def input_string(new_message):
    """
    Prompts the user to enter a string input and returns it
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_message: The message to be prompted to the user.
    :return: User's string input
    :precondition: None
    :postconidtion: A valid string is entered by the user
    :complexity time: O(N) where N = Number of user inputs until a string is entered
    """
    # loops till the user enter a string
    while True:
        try:
            return str(input(new_message))
        except ValueError:
            print("Invalid input: Please enter an Integer.")


def command_append(new_list=[]):
    """
    Append an item from the user input to the list and return it
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list for the user input item to be appended
    :return: Updated list with the user item appended
    :precondition: None. Usually the precondition is that the new_list is not none or null though this is overcome through assigning a default value to new_list as shown above. Thus there is no longer a precondition required as the function or method can be invoked with or without the list.
    :postconidtion: A list (not null/ none) is returned
    :complexity time: O(N)  where   N = Number of user inputs until a string is entered by the user (from the input_string)
    """
    try:
        current_item = input_string("Append item: ")
        # added a print line just for checking
        # print(current_item)
        new_list.append(current_item)
        print("Item appended.")
        return new_list
    # example of an unknown exception handling
    except:
        print("Error: Unable to append item to list.")
        # need to return the original list if the operation fail
        return new_list


def command_sort(new_list=[]):
    """
    Sort the list according to the order of normal.
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list to be sorted
    :return: sorted list
    :precondition: None
    :postconidtion: A not None/ Null list is returned
    :complexity time: O(N)    where   N = Complexity of the sorting() algorithm
    """
    try:
        # print(new_list)
        # new_list = new_list.sort(None, None, new_reverse) doesnt work for strings
        new_list.sort()
        print("List sorted.")
        return new_list
    except:
        print("Error: Unable to sort list.")
        return new_list


def command_print(new_list=[]):
    """
    Prints out the list
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list to be printed out
    :return: None
    :precondition: None
    :postconidtion: Prints out to the user
    :complexity time: O(1)
    """
    try:
        print(new_list)
    except:
        print("Error: Unable to print list.")


def command_quit():
    """
    Quit the program
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :return: None
    :complexity time: O(1)
    :precondition: None
    :postconidtion: Program exits
    """
    print("Exiting program.")
    raise SystemExit


def command_clear(new_list=[]):
    """
    Clears the list
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list to be cleared
    :return: A cleared list
    :precondition: None
    :postconidtion: A not None/ Null list is returned
    :complexity time: O(1)
    """
    try:
        new_list.clear()
        print("List cleared.")
        return new_list
        # optionally
        # return []
    except:
        print("Error: Unable to clear list.")
        return new_list


def command_reverse(new_list=[]):
    """
    Reverses the list
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list to be reversed
    :return: A reversed list
    :precondition: None
    :postconidtion: A not None/ Null list is returned
    :complexity time: O(N)    where   N = Complexity of the reverse() function
    """
    try:
        # reverse the list
        new_list = new_list[::-1]
        print("List reversed.")
        return new_list
    except:
        print("Error: Unable to reverse list.")
        return new_list


def command_pop(new_list=[]):
    """
    Pops (remove) and prints the last element of the list.
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list to be popped.
    :return: A list with the last element popped. None if the list is empty
    :precondition: None
    :postconidtion: A not None/ Null list is returned
    :complexity time: O(1)
    """
    try:
        # checks if the list is empty
        # can only pop non-empty list
        if len(new_list) > 0:
            current_item = new_list.pop()
            print("Popped: " + str(current_item))
            return new_list
        else:
            print("Error: List is empty and thus there is nothing to pop.")
            # still need to return the list to the original list in the main()
            return new_list
    except:
        print("Error: Unable to pop list.")
        return new_list


def command_size(new_list=[]):
    """
    Prints out the size of the list and return it
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list for the size to be known
    :return: The size of the list
    :precondition: None
    :postconidtion: Prints out the size if able with a return of size for future use
    :complexity time: O(1)
    """
    try:
        current_size = len(new_list)
        # always a good practice to convert to string before printing
        print("Size of list: " + str(current_size))
        return current_size
    except:
        print("Error: Unable to obtain size of list.")


def command_insert(new_list=[]):
    """
    Insert an item before the given index of the list
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list to be inserted
    :return: The list with a new item inserted
    :precondition: None
    :postconidtion: A not None/ Null list is returned
    :complexity time: O(N+M)    where   N = Number of user inputs until a string as item is entered
                                        M = Number of user inputs until a valid index is entered
    :note: Used as an example demonstrate time complexity
    """
    try:
        # get item
        current_item = input_string("Please enter the item to be inserted: ")
        # initialize index for the loop
        current_index = len(new_list) + 1
        # as long as the index is invalid
        while current_index < 0 or current_index > len(new_list):
            current_index = input_integer("Please enter the index for the item to be inserted: ")
            # informs the user that the index is invalid
            if current_index < 0 or current_index > len(new_list):
                print("Error: Index entered is out of boundary of list. Please enter a index from 0 to " + str(len(new_list)))

        # inserts
        new_list.insert(current_index, current_item)
        print("Item " + str(current_item) + " inserted at index " + str(current_index) + ".")
        return new_list
    except:
        print("Error: Unable to insert item to list.")
        return new_list


def command_find(new_list=[]):
    """
    Finds the first occurence of a user entered item in the list, prints and return it. Print and return false if item is not found.
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :param new_list: The list for the user to search
    :return: Prints out the index of the first occurence of the item in the list and return it. Prints and return false if item is not found.
    :precondition: The elements in the list are strings to be consistent with the append and insert method. Thus the search or find need to look for strings
    :postconidtion: The index or false if item is not found
    :complexity time: O(N)    where   N = Complexity of the index() function
    """
    try:
        current_item = input_string("Item to find in the list: ")
        current_index = new_list.index(current_item)
        print("Item found at index: " + str(current_index))
        return current_index
    except:
        print("Error: Unable to find item " + str(current_item) + " in list.")
        return False


def main():
    """
    The main method to run the menu
    :author:    Ian Lim
    :since:     20140805
    :modified:  20140810
    :precondition: None
    :postconidtion: None
    :return: None
    :complexity (time): O(N*M)  where   N = Number of user commands
                                        M = Highest complexity of the commands
    """
    print("Running the Main program - Menu!")
    current_list = []
    while(True):
        print_menu()
        current_command = input_string("Please enter the command: ")
        print(current_command)
        if current_command == str(1):
            current_list = command_append(current_list)
        elif current_command == str(2):
            current_list = command_sort(current_list)
        elif current_command == str(3):
            command_print(current_list)
        elif current_command == str(4):
            command_quit()
        elif current_command == str(5):
            current_list = command_clear(current_list)
        elif current_command == str(6):
            current_list = command_reverse(current_list)
        elif current_command == str(7):
            current_list = command_pop(current_list)
        elif current_command == str(8):
            command_size(current_list)
        elif current_command == str(9):
            current_list = command_insert(current_list)
        elif current_command == str(10):
            command_find(current_list)
        else:
            print("Error: Invalid command.")


# Run the main (assumes that the main the module is the menu and the earlier two examples are just functions
# Uncomment to run menu
main()
