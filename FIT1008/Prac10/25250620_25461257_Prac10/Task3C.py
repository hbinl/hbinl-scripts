'''
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified: 20141015
'''
import Task3B
Task3B.main()

def main():
    inputfile = input('Enter the file to be read: ')
    outputfile = input('Enter the file to be written: ')
    convert(inputfile, outputfile)

def convert(inputfile, outputfile):
    '''
    @precondition: a valid file
    @postcondition: none

    @param: inputfile, outputfile

    @complexity: O(N) where N is the number of binary digits
    '''
    try:
        reading = open(inputfile, 'r')
        writing = open(outputfile, 'w')
        while True:
            read = reading.read(7)
            if read == '':
                break
            read = iter(read)
            item = Task3B.tree.printing(read)
            writing.write(item)
        reading.close()
        writing.close()
    except FileNotFoundError:
        print('Error. Please enter a valid file to read.')

if __name__ == "__main__":
    main()

#Test functions

def test_convert():
    print('Testing for finding an item in the binary tree with a file containing a valid binary string.')
    convert('Binary.txt', 'Task3C.Output1.txt')
    print('Test success.')
    print('\nTesting for finding an item in the binary tree with a non-existing file.')
    convert('No.txt', 'Task3C.Output2.txt')
    print('Test success.')
    print('\nTesting for finding an item in the binary tree with a file containing non-binary string.')
    try:
        convert('Alphabet.txt', 'Task3C.Output3.txt')
    except:
        print('Error. File is already in alphabets.')
    print('Test success.')
    
