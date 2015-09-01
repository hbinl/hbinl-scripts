"""
FIT1008 Prac 10 Advanced Task
Loh Hao Bin 25461257
@purpose: Morse Code
@created 20141011
@modified 20141011
"""

from Task1 import *
from Task2 import *
from Task3 import *



def morse_io_encode():
    input_filename = str(input("Input: "))
    output_filename = str(input("Output: "))
    input_file = read_file(input_filename)
    output = morse_io_encode_aux(input_file)
    write_file(output_filename, output)

def morse_io_encode_aux(file):
    file.seek(0)
    end = False
    output = ''
    morse_list = morse_list_constructor()
    while not end:
        c = file.read(1)
        if c == '':
            end = True
        else:
            output += str(morse_list[c])
            output += '000'
    #print(output)
    return output

def morse_io_decode():
    '''
        @purpose:
    '''
    mtree = morse_tree()
    input_filename = str(input("Input: "))
    output_filename = str(input("Output: "))
    input_file = read_file(input_filename)
    converted = morse_split(input_file)
    output = ''
    for x in converted:
        c_node = mtree.getNode(x)
        c = mtree.getNode_item(c_node)
        output += c
    #print(output)
    write_file(output_filename, output)

def morse_tree():
    mtree = BinaryTree()
    morse_list = morse_list_constructor()
    for c in 'abcdefghijklmnopqrstuvwxyz 1234567890':
        mtree.add(c, iter(morse_list[c]))
    return mtree


def morse_list_constructor():
    morse_list = {
        "a" : ".-",
        "b" : "-...",
        "c" : "-.-.",
        "d" : "-..",
        "e" : ".",
        "f" : "..-.",
        "g" : "--.",
        "h" : "....",
        "i" : "..",
        "j" : ".---",
        "k" : "-.-",
        "l" : ".-..",
        "m" : "--",
        "n" : "-.",
        "o" : "---",
        "p" : ".--.",
        "q" : "--.-",
        "r" : ".-.",
        "s" : "...",
        "t" : "-",
        "u" : "..-",
        "v" : "...-",
        "w" : ".--",
        "x" : "-..-",
        "y" : "-.--",
        "z" : "--..",
        " " : ".......",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----"
        }
    for c in 'abcdefghijklmnopqrstuvwxyz 1234567890':
        morse_list[c] = morse_parse(morse_list[c])
    #print(morse_list)
    return morse_list

def morse_parse(string):
    output = ''
    for i in range(len(string)):
        if string[i] == '.':
            output += '1'
        elif string[i] == '-':
            output += '111'
        output += '0'
    return output[0:len(output)-1]



def morse_split(file):
    file.seek(0)
    end = False
    output = ''
    final = []
    zero_count = 0
    while not end:

        c = file.read(1)

        if c == '':
            end = True
        else:
            if c == '0':
                zero_count += 1
                output += c
                if zero_count == 3:
                    output = output[0:len(output)-3]
                    final.append(output)
                    zero_count = 0
                    output = ''
            else:
                zero_count = 0
                output += c
    return final

def text_ascii_morse():
    input_filename = str(input("Input: "))
    output_filename_ascii = str(input("Output-ASCII: "))
    output_filename_morse = str(input("Output-Morse: "))
    input_file = read_file(input_filename)
    processed = convert_min(input_file)
    write_file('test-min.txt', processed)

    output_ascii = convert_to_ascii(read_file('test-min.txt'))
    write_file(output_filename_ascii, output_ascii)
    output_morse = morse_io_encode_aux(read_file('test-min.txt'))
    write_file(output_filename_morse, output_morse)

def morse_io_menu():
    quit = False
    btree = BinaryTree()
    while not quit:
        try:
            print("1. Encode a minimised file into Morse Code")
            print("2. Decode into Morse Code")
            print("3. Minimise, and encode in both ASCII and Morse")
            print("4. Quit")
            cmd = int(input(">> "))
            if cmd == 1:
                morse_io_encode()
            elif cmd == 2:
                morse_io_decode()
            elif cmd == 3:
                text_ascii_morse()
            elif cmd == 4:
                quit = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid command")
        except FileNotFoundError:
            print("File not found.")
        except IndexError:
            print("File error.")

if __name__ == "__main__":
    try:
        morse_io_menu()
    except KeyboardInterrupt:
        print()

