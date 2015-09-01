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
        morse_list[c] = code
    return morse_list

def alt_encoding(histogram):
    btree = BinaryTree()
    dict = morse_list_constructor_binary()
    histogram = histogram[::-1]
    for i in range(0,len(histogram),2):
        btree.add(histogram[i][0], dict[histogram[i]]


def s_encode_helper():
    input_filename = str(input("Original input: "))
    file = read_file(input_filename)
    histogram = sort_count(file)
    encoding_tree = alt_encoding(histogram)


if __name__ == "__main__":
    try:

        s_encode_helper()
    except KeyboardInterrupt:
        print()

