'''
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified: 20141015
'''

import ClassTree
tree = ClassTree.BinaryTree()

def main():
    end = False
    while not end:
        print('1. Add')
        print('2. Get')
        print('3. Print')
        print('4. Quit')
        command = input('Enter a command: ')
        try:
            command = int(command)
            if command == 1:
                item = input('Enter an item to be inserted into the Binary Tree: ')
                binary_str = input('Enter the position of the item: ')
                adding(item, binary_str)
            elif command == 2:
                binary_str = input('Enter the position of the item to be printed: ')
                getting(binary_str)
            elif command == 3:
                printing()
            elif command == 4:
                end = True
            else:
                print('Error. Please enter a valid command.')
        except:
            print('Error. Please enter a valid command.')

def adding(item, binary_str):
    '''
    @precondition: a binary string
    @postcondition: an item is added to the binary tree

    @param: binary_str

    @complexity: O(N) where N is the number of binary digits
    '''
    valid = True
    for i in binary_str:
        if i != '0' and i != '1':
            valid = False
    if valid:
        binary_str = iter(binary_str)
        tree.add(item, binary_str)
    else:
        print('Error. Please enter a binary string.')

def getting(binary_str):
    '''
    @precondition: a binary string
    @postcondition: none

    @param: binary_str

    @complexity: O(N) where N is the number of binary digits
    '''
    valid = True
    for i in binary_str:
        if i != '0' and i != '1':
            valid = False
    if valid:
        binary_str = iter(binary_str)
        print(tree.printing(binary_str))
    else:
        print('Error. Please enter a valid position.')

def printing():
    '''
    @precondition: none
    @postcondition: none

    @param: none

    @complexity: O(N) where N is the number of nodes in the binary tree
    '''
    tree.print_all()

if __name__ == "__main__":
    main()

#Test functions

def reset_tree():
    tree = ClassTree.BinaryTree()

def test_adding():
    reset_tree()
    print('Testing for adding an item into position 01')
    adding('Hello', '01')
    tree.print_all()
    print('Test success.')
    print('\nTesting for adding an item into a position 01 which already contains an item.')
    adding('Replaced', '01')
    tree.print_all()
    print('Test success.')
    print('\nTesting for adding an item into no position')
    adding('Bye', ' ')
    print('Test success.')
    print('\nTesting for adding an item into an invalid position 02')
    adding('Nooooo', '02')
    print('Test success.')

def test_getting():
    reset_tree()
    print('Testing for an item in position 01 which contains something')
    adding('Hello', '01')
    getting('01')
    print('Test success.')
    print('\nTesting for an item in a position that contains nothing')
    try:
        getting('101')
    except:
        print('Error. Position contains nothing.')
    print('Test success.')
