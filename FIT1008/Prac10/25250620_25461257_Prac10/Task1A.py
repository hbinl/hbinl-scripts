"""
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified:20141015
"""

def main():
    inputfile = input('Enter a file name which you want to count the number of characters: ')
    read(inputfile)

def read(inputfile):
    '''
    @precondition: a valid input file
    @postcondition: none

    @param: inputfile

    @complexity:
    Best case: O(1) where the file does not exist
    Worse case: O(N) where N is the number of characters in the file
    '''
    try:
        reading = open(inputfile, 'r')
        count = 0
        read = reading.read()
        read = read.split('\n')
        for i in read:
            for j in i:
                if j != ' ':
                    count = count + 1
        print(count)
    except:
        print('Error. Please enter a valid file to count the number of characters.')

if __name__ == '__main__':
    main()

#Test functions

def test():
    print('Testing for reading Random.txt which contains characters')
    read('Random.txt')
    print('Test success.')
    print('\nTesting for reading Empty.txt which is an empty file')
    read('Empty.txt')
    print('Test success.')
    print('\nTesting for counting the number of characters in a non-existence file')
    read('No.txt')
    print('Test success.')
