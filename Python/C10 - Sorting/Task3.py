"""
FIT1008 Prac 10 Task 3
Loh Hao Bin 25461257, Kedryn Yeo 25250620
@purpose: Binary Tree
@created 20141011
@modified 20141011
"""

from Task1 import *
from Task2 import *

def convert_to_ascii(file):
    '''
        @purpose: Converts all the characters in the file into ASCII binary form
        @complexity: O(n) where n is length of file
        @parameter: file - the file object
        @precondition: A file object is passed
        @postcondition: A string containing all the characters in ASCII binary
    '''
    file.seek(0)
    end = False
    output = ''
    while not end:
        c = file.read(1)
        if c == '':
            end = True
        else:
            ascii = ord(c)
            bin = dec_to_binary(ascii)
            output += bin

    return output

def dec_to_binary(dec):
    '''
        @purpose: Convert decimal number to 8-bit binary
        @complexity: O(1)
        @parameter: dec - the decimal integer to be converted
    '''
    return "{0:08b}".format(dec)

def binary_to_dec(binary):
    '''
        @purpose: Convert binary to decimal number
        @complexity: O(1)
        @parameter: binary - the binary to be converted
    '''
    return int("{0:d}".format(int(binary,2)))

def ascii_aux():
    '''
        @purpose: Helper function for Task 3 Part i
    '''
    input_filename = str(input("Input: "))
    output_filename = str(input("Output: "))
    input_file = read_file(input_filename)
    converted = convert_to_ascii(input_file)
    write_file(output_filename, converted)


def convertback_btree():
    '''
        @purpose: Helper function for Task 3 part iii
    '''
    input_filename = str(input("Input: "))
    output_filename = str(input("Output: "))
    input_file = read_file(input_filename)
    btree = construct_ascii_btree()
    converted = file_to_string(input_file, btree)
    write_file(output_filename, converted)


def file_to_string(file, btree):
    '''
        @purpose: Convert each 8 bit binary back into their character form
        @complexity: O(n) where n is length of file
        @parameter:
            file: The file to be converted back
            btree: the binary tree with items as reference
        @precondition: A file object, and a reference binary tree
        @postcondition: Returns a string converted back into character form
    '''
    file.seek(0)
    end = False
    output = ''
    while not end:
        c = str(file.read(8))
        if c == '':
            end = True
        else:
            c_iter = iter(c)
            char_node = btree.getNode(c_iter)
            char = btree.getNode_item(char_node)
            output += char
    return output


def construct_ascii_btree():
    '''
        @purpose: Construct a binary tree with a-z inserted in place
        @complexity: O(n) where n is the length of items to be inserted
        @parameter: None
        @precondition: None
        @postcondition: Returns a dictionary binary tree
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890'
    btree = BinaryTree()

    for c in letters:
        bin_c = dec_to_binary(ord(c))
        bin_ascii = iter(str(bin_c))
        btree.add(c, bin_ascii)

    #adding space characters and line breaks
    btree.add(' ', iter(str(dec_to_binary(32))) )
    btree.add('\n', iter(str(dec_to_binary(10))) )

    return btree

def t3_menu():
    quit = False
    btree = BinaryTree()
    while not quit:
        try:
            print("\n1. Convert to ASCII")
            print("2. Convert from ASCII")
            print("3. Quit")
            cmd = int(input(">> "))
            if cmd == 1:
                ascii_aux()
            elif cmd == 2:
                convertback_btree()
            elif cmd == 3:
                quit = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid command")
        except FileNotFoundError:
            print("File not found.")

if __name__ == "__main__":
    try:
        t3_menu()
    except KeyboardInterrupt:
        print()

