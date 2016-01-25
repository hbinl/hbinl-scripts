"""
FIT1008 Prac 10 Task 2
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: Binary Tree
@created 20141010
@modified 20141010
"""

class TreeNode:
    def __init__(self, item, left, right):
        self.item = item
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, item, binary_str_itr):
        '''
        @purpose: Add an item into the binary tree at node specified by the bitlist
        @complexity: O(n) where n is the length of the bitlist
        @parameter: Item: the item to be added; binary_str_itr: the bitlist iterator of location
        @precondition: BinaryTree object initialised
        @postcondition: The item added at the location specified
        '''
        self.root = self.add_aux(self.root, item, binary_str_itr)

    def add_aux(self, current, item, binary_str_itr):
        '''
        @purpose: Auxiliary recursive function for .add()
        @complexity: O(n) where n is the length of the bitlist
        @parameter: current - Current node
                    item - Item to be added
                    binary_str_itr - An iterator object formed from bitlist
        @precondition: BinaryTree object initialised, and called by .add()
        @postcondition: The item added at location specified, and returns the current node
        '''
        if current is None:
            current = TreeNode(None, None, None)

        try:
            bit = next(binary_str_itr)
            #print(bit)
            if bit == '0':
                current.left = self.add_aux(current.left, item, binary_str_itr)
            elif bit == '1':
                current.right = self.add_aux(current.right, item, binary_str_itr)
        except StopIteration:
            current.item = item

        return current


    def getNode_item(self, node):
        '''
        @purpose: Returns the item in the node
        @complexity: O(1)
        @parameter: Node: the node to obtain item from
        @precondition: Binary tree object initialised
        @postcondition: Returns the item in the node
        '''
        return node.item


    def getNode(self, binary_str):
        '''
        @purpose: Recursive get node specified by the bitlist
        @complexity: O(n) where n is length of bitlist
        @parameter: binary_str - a valid binary string
        @precondition: Binarytree object initialised
        @postcondition: Returns the node requested
        '''
        # converts the bit list into an iterator
        binary_str = iter(binary_str)
        node = self.getNode_aux(self.root, binary_str)
        return node

    def getNode_aux(self, current, binary_str_itr):
        '''
        @purpose: Recursively get the node specified
        @complexity: O(n) where n is the length of bitlist
        @parameter: current: the current node
                    binary_str_itr: An iterator formed from bitlist
        @precondition: Binarytree Object initialised
        @postcondition: Returns the node requested
        '''
        if current != None:
            try:
                bit = next(binary_str_itr)

                if bit == '0' and current.left != None:
                    node = self.getNode_aux(current.left, binary_str_itr)
                elif bit == '1' and current.right != None:
                    node = self.getNode_aux(current.right, binary_str_itr)
                else:
                    raise IndexError
            except StopIteration:
                node = current
        else:
            raise IndexError

        return node

    def inorder_print(self):
        '''
        @purpose: Recursively do an in-order traversal of the binary tree
        @complexity: O(n) where n is the number of items in the tree
        @parameter: None
        @precondition: Binary Tree object initialised
        @postcondition: Prints the items in the tree in-orderly
        '''
        self.inorder_print_aux(self.root)

    def inorder_print_aux(self,current):
        '''
        @purpose: Auxiliary recursive function for in-order-traversal
        @complexity: O(n) where n is the number of items in the tree
        @parameter: Current: the current node
        @precondition: Binary tree object initialised
        @postcondition: Perform in order traversal on the binary tree and prints out the nodes
        '''
        if current is not None:
            self.inorder_print_aux(current.left)
            if current.item != None:
                print(current.item)
            self.inorder_print_aux(current.right)




def menu_add(btree):
    '''
        @purpose: The menu helper for Add
    '''
    item = input("Item: ")
    binary_str = iter(str(input("Binary String: ")))
    btree.add(item, binary_str)
    return btree


def menu_get(btree):
    '''
        @purpose: Menu helper for get
    '''
    binary_str = iter(str(input("Binary String: ")))
    node = btree.getNode(binary_str)
    print(btree.getNode_item(node))


def menu_print(btree):
    '''
        @purpose: Menu helper for print
    '''
    btree.inorder_print()

def menu():
    quit = False
    btree = BinaryTree()
    while not quit:
        try:
            print("\n1. add item binary_str")
            print("2. get binary_str")
            print("3. print")
            print("4. quit")
            cmd = int(input(">> "))
            if cmd == 1:
                btree = menu_add(btree)
            elif cmd == 2:
                menu_get(btree)
            elif cmd == 3:
                menu_print(btree)
            elif cmd == 4:
                quit = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid command")

def t2_test_add():
    print('\nAdd')
    btree = BinaryTree()
    btree.add('a', iter('10101'))
    btree.add('b', iter('10111'))
    print(btree.getNode_item(btree.getNode('10101')))
    print(btree.getNode_item(btree.getNode('10111')))
    btree.add('b', iter('12'))
    try:
        print(btree.getNode_item(btree.getNode('12')))
    except IndexError:
        print("Invalid binary string.")


def t2_test_inordertraversal():
    print('\nIn order traversal')
    btree = BinaryTree()
    btree.add('a', iter('10101'))
    btree.add('b', iter('10111'))
    btree.add('c', iter('01'))
    btree.add('d', iter('0'))
    btree.add('x', iter('010'))
    btree.inorder_print()


if __name__ == "__main__":
    try:
        t2_test_add()
        t2_test_inordertraversal()
        #menu()
    except KeyboardInterrupt:
        print()