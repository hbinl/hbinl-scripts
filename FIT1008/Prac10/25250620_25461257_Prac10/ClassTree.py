'''
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified: 20141015
'''
class TreeNode:
    '''
    Creates a date structure to store the tree nodes of a binary tree

    Attributes:
    item = An item in the tree
    right = The right child node
    left = The left child node

    Methods:
    __str__: Changes the item to a string
    '''
    def __init__(self, item, left, right):
        self.item = item
        self.right = right
        self.left = left

    def __str__(self):
        '''
        @precondition: none
        @postcondition: Returns the item in string form

        @param: none

        @complexity: O(1)
        '''
        return str(self.item)

class BinaryTree:
    '''
    Creates a binary tree

    Attribute:
    root = The head of the tree

    Methods:
    add = Adds an item onto the binary tree
    add_aux = Adds an item onto the binary tree
    printing = Prints an item in the binary tree according to the position 
    print_aux = Prints an item in the binary tree according to the position 
    print_all = Prints all items in the binary tree
    print_all_aux = Prints all items in the binary tree
    '''
    def __init__(self):
        self.root = None

    def add(self, item, binary_str_itr):
        '''
        @precondition: none
        @postcondition: an item added onto the binary tree

        @param: item, binary_str_itr

        @complexity: O(N) where N is the number of binary digits
        '''
        self.root = self.add_aux(self.root, item, binary_str_itr)

    def add_aux(self, current, item, binary_str_itr):
        '''
        @precondition: none
        @postcondition: an item added onto the binary tree

        @param: current, item, binary_str_itr

        @complexity: O(N) where N is the number of binary digits
        '''
        if current is None:
            current = TreeNode(None, None, None)
        try:
            bit = next(binary_str_itr)
            if bit == '0':
                current.left = self.add_aux(current.left, item, binary_str_itr)
            elif bit == '1':
                current.right = self.add_aux(current.right, item, binary_str_itr)
        except StopIteration:
            current.item = item
        return current

    def printing(self, binary_str_itr):
        
        '''
        @precondition: none
        @postcondition: none

        @param: binary_str_itr

        @complexity: O(N) where N is the number of binary digits
        '''
        return self.print_aux(self.root, binary_str_itr)

    def print_aux(self, current, binary_str_itr):
        '''
        @precondition: none
        @postcondition: none

        @param: current, binary_str_itr

        @complexity: O(N) where N is the number of binary digits
        '''
        try:
            bit = next(binary_str_itr)
            if bit == '0':
                return self.print_aux(current.left, binary_str_itr)
            elif bit == '1':
                return self.print_aux(current.right, binary_str_itr)
        except StopIteration:
            return current.item
        
    def print_all(self):
        '''
        @precondition: none
        @postcondition: none

        @param: none

        @complexity: O(N) where N is the number of items in the binary tree
        '''
        self.print_all_aux(self.root)

    def print_all_aux(self, current):
        '''
        @precondition: none
        @postcondition: none

        @param: current

        @complexity: O(N) where N is the number of items in the binary tree
        '''
        if current is not None:
            self.print_all_aux(current.left)
            if current.item is not None:
                print(current)
            self.print_all_aux(current.right)
            
#Test functions

tree = BinaryTree()

def tree_reset():
    tree = BinaryTree()

def test_add():
    tree_reset()
    print('Testing for adding an item onto the binary tree at position 01.')
    tree.add('Hello', iter('01'))
    tree.print_all()
    print('Test success.')
    print('\nTesting for adding an item at no position.')
    tree.add('Bye', iter(' '))
    tree.print_all()
    print('Error. Please enter a position.')
    print('Test success.')
    print('\nTesting for adding and item onto the binary tree at a position 01 that already has an item.')
    tree.add('Replaced', iter('01'))
    tree.print_all()
    print('Test success.')
    print('\nTesting for adding an item onto the binary tree at an invalid position 02.')
    tree.add('Abc', iter('02'))
    tree.print_all()
    print('Error. Please enter a valid binary string.')
    print('Test success.')
    
def test_printing():
    tree_reset()
    print('Testing for printing an item from the binary tree at position 01.')
    tree.add('Hello', iter('01'))
    print(tree.printing(iter('01')))
    print('Test success.')
    print('\nTesting for printing an item from the binary tree at no position.')
    tree.add('Bye', iter(' '))
    print(tree.printing(iter(' ')))
    print('Test success.')
    print('\nTesting for printing an item from the binary tree at a position which contains no item.')
    try:
        print(tree.printing(iter('101')))
    except:
        print('Error. Position contains nothing.')
    print('Test success.')

def test_print_all():
    tree_reset()
    print('Testing for printing empty binary tree.')
    tree.print_all()
    print('Nothing in the tree to print,')
    print('Test success.')
    print('\nTesting for printing a binary tree containing Hello Hi Bye.')
    tree.add('Hello', iter('00'))
    tree.add('Hi', iter('01'))
    tree.add('Bye', iter('10'))
    tree.print_all()
    print('Test success.')
