'''
@author: Kedryn Yeo Ju Lin 25250620 and Loh Hao Bin 25461257
@since: 20141012
@modified: 20141015
'''
def main():
   inputfile = input('Enter the file to be read: ')
   outputfile = input('Enter the file to be written: ')
   code(inputfile, outputfile)

def code(inputfile, outputfile):
   '''
   @precondition: a valid input file
   @postcondition: none

   @param: inputfile, outputfile

   @complexity:
   Best case: O(1) where the file does not exist
   Worse case: O(N) where N is the number of characters in the input file
   '''
   try:
      reading = open(inputfile, 'r')
      writing = open(outputfile, 'w')
      read = reading.read()
      for i in read:
         if i.isalpha():
            i = ord(i)
            i = bin(i)[2:]
            writing.write(str(i))
      reading.close()
      writing.close()
   except:
      print('Error. Please enter a valid file to read.')

if __name__ == "__main__":
   main()
   
#Test functions

def test_code():
   print('Testing for a file containing characters.')
   code('Random.txt', 'Task3A.Output1.txt')
   print('Test success.')
   print('\nTesting for a file which does not exist.')
   code('No.txt', 'Task3A.Output2.txt')
   print('Test success.')
