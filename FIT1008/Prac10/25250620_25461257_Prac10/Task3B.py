'''
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified: 20141015
'''
import ClassTree
tree = ClassTree.BinaryTree()

def main():
    '''
    @precondition: none
    @posticondition: a binary tree containing alphabets at positions specified by their ASCII code

    @param: none
    
    @complexity: O(N) where N is the number of alphabets
    '''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        ascii = ord(i)
        ascii = bin(ascii)[2:]
        ascii = iter(ascii)
        tree.add(i, ascii)

if __name__ == "__main__":
    main()

#Test functions

def test_main():
    print('Testing for finding an item at position 1100001.')
    print(tree.printing(iter('1100001')))
    print('Test success.')
    print('\nTesting for finding an item at a position which does not contain an item.')
    try:
        print(tree.printing(iter('000')))
    except:
        print('Error. There is no item at position 000.')
    print('Test success.')
    
