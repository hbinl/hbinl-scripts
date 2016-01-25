"""
FIT1008 Prac 10 Advanced Task 2
Loh Hao Bin 25461257
@purpose: Encoding using gray code representations
@created 20141011
@modified 20141011
"""

from Task1 import *
from Task2 import *
from Task3 import *

def alt_morse_io_menu():
    quit = False
    btree = BinaryTree()
    while not quit:
        try:
            print("1. Encode a minimised file into Alt_Morse")
            print("2. Decode from Alt_Morse")
            print("3. Quit")
            cmd = int(input(">> "))
            if cmd == 1:
                s_encode_helper()
            elif cmd == 2:
                s_decode_helper()
            elif cmd == 3:
                quit = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid command")
        except FileNotFoundError:
            print("File not found.")
        except IndexError:
            print("File error.")

def morse_list_constructor_binary():
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
        }
    for c in 'abcdefghijklmnopqrstuvwxyz':
        code = morse_list[c]
        code = code.replace(".","1")
        code = code.replace("-","0")
        code = "1" + code
        morse_list[c] = code.zfill(5)
    return morse_list

def alt_decoding_tree():
    btree = BinaryTree()
    dict = morse_list_constructor_binary()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        btree.add(c, iter(dict[c]))
    return btree


def s_decode_helper():
    input_filename = str(input("Original input: "))
    file = read_file(input_filename)
    decoding_tree = alt_decoding_tree()
    print("Decoding...")
    decoded = s_decode(file, decoding_tree)
    output_filename = str(input("Output: "))
    write_file(output_filename, decoded)

def s_decode(file, decoding_tree):
    file.seek(0)
    end = False
    output = ''
    while not end:
        c = file.read(5)
        if c == '':
            end = True
        else:
            output += str(decoding_tree.getNode_item(decoding_tree.getNode(c)))
    return output


def s_encode(file):
    file.seek(0)
    dict = morse_list_constructor_binary()
    end = False
    output = ''
    while not end:
        c = file.read(1)
        if c == '':
            end = True
        else:
            output += dict[c]
    return output

def s_encode_helper():
    input_filename = str(input("Original input: "))
    file = read_file(input_filename)
    print("Encoding...")
    encoded = s_encode(file)
    output_filename = str(input("Output: "))
    write_file(output_filename, encoded)

if __name__ == "__main__":
    try:
        alt_morse_io_menu()
    except KeyboardInterrupt:
        print()

