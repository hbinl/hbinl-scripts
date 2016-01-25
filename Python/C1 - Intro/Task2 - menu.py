"""
Task 2
@purpose This program is for list manipulation using menus.
@author Loh Hao Bin 25461257
@since 20140803
@modified 20140806
@Precondition: The user inputs a command from the list provided.
@Postcondition: Depending on the command
"""

def print_menu():
       """
       @purpose for printing the menu
       @Complexity O(1)
       """
       print('\nMenu:')
       print('1. Append')
       print('2. Sort')
       print('3. Print')
       print('4. Quit')
       print('5. Clear')
       print('6. Reverse')
       print('7. Pop')
       print('8. Size')
       print('9. Insert')
       print('10. Find')


#MAIN BLOCK START
#my_list = ["a", "g", "c", "x", "f", "d", "b", "v", "z"] #testing
my_list = []
quit = False
input_line = None

while not quit:
    #displays the menu
    print_menu()

    try:
        command = int(input("\nEnter command: "))

        if command == 1:
            #Append command
            item = input("Item? ")
            my_list.append(item)
            print(my_list)

        elif command == 2:
            #Sort command
            my_list.sort()
            print(my_list)

        elif command == 3:
            #print command
            print(my_list)

        elif command == 4:
            #quit
            quit = True

        elif command == 5:
            #Clear command
            #asks for confirmation on clearing list
            confirm = str(input("Are you sure you want to clear the list? (Y/N): "))
            if confirm == "Y" or confirm == "y":
                my_list = []
                print("List cleared.")
            elif confirm == "N" or confirm == "n":
                print("Operation cancelled.")
            else:
                print("Please input Y or N for the answer.")

        elif command == 6:
            #Reverse command
            """my_list.reverse()     #alternative to the slicing method"""

            my_list = my_list[::-1] #reverses the list, slice with third parameter being step
            print(my_list)

        elif command == 7:
            #pop
            last = my_list.pop()
            print(last)

        elif command == 8:
            #size
            print("The length of the list is " + str(len(my_list)))

        elif command == 9:
            #Insert
            insert_item = input("Please enter the item: ")
            try:
                insert_index = int(input("Please enter the position you would like to insert at: "))
                my_list.insert(insert_index, insert_item)
                print(my_list)
            except ValueError: #catching cases where user inputs things other than numbers
                print("Please enter a valid index number.")


        elif command == 10:
            #Find command
            """ Alternative solution using .index()
            try:
                find_item = (input("Please enter the item to find: "))
                print(my_list.index(find_item))
            except ValueError:
                print("False")
            """

            #sequential search on the list
            #@Complexity: O(N)
            find_item = (input("Please enter the item to find: "))
            found = False
            for i in range(0,len(my_list)):
                if my_list[i] == find_item:
                    print(i)
                    found = True
                    break
            if found == False:
                print("False")

        else:
            #any other numbers inserted
            print("Please enter a valid command.")


    except ValueError:  #catching invalid number errors
        print("Please enter a valid command number.")

    except TypeError: #catch sorting between int and str type errors
        print("The data types do not match.")

    except IndexError: #catch indexerrors
        print("The list is either empty or the index specified does not exist.")