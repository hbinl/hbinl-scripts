"""
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified: 20141015
"""

def main():
    inputfile = input('Enter the file to be read: ')
    outputfile = input('Enter the file to be written: ')
    lower(inputfile, outputfile)

def lower(inputfile, outputfile):
    '''
    @precondition: a valid input file
    @postcondition: an output file is created which contains all characters in the input file in lowercase form

    @param: inputfile, outputfile
    
    @complexity:
    Best case: O(1) where the file does not exist
    Worst case: O(N) where N is the number of characters in the file
    '''
    try:
        reading = open(inputfile, 'r')
        writing = open(outputfile, 'w')
        readfile = reading.read()
        for i in readfile:
            if i.isalpha():
                i = i.lower()
                writing.write(i)
        reading.close()
        writing.close()
    except:
        print('Error. Please enter a valid file to read.' )
        
if __name__ == "__main__":
    main()

#Test functions

def test():
    print('Testing for reading Random.txt that contains characters and then writing it to Output1.txt')
    lower('Random.txt', 'Task1B.Output1.txt')
    print('Test success.')
    print('\nTesting for reading Empty.txt which is an empty file and then writing it to Output2.txt')
    lower('Empty.txt','Task1B.Output2.txt')
    print('Test success.')
    print('\nTesting for reading a non-existence file and then writing it to Output3.txt')
    lower('No.txt', 'Task1B.Output3.txt')
    print('Test success.')
