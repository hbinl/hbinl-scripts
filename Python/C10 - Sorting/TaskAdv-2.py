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


def generate_bitstring(n):
    seed = [0,1]
    for i in range(n-1):
        seed = seed + seed[::-1]
        c = 2 ** (i+1)
        for j in range(c):
            seed[j] = str('0') + str(seed[j])
        for j in range(c, c*2):
            seed[j] = str('1') + str(seed[j])
        #print(seed)
        c += 1
    return seed

def generate_dictionary():
    dictionary = {}
    bitstr = generate_bitstring(5)
    i = 0
    for c in 'abcdefghijklmnopqrstuvwxyz':
        dictionary[c] = bitstr[i]
        i += 1
    return dictionary

def alt_encode(file):
    dictionary = generate_dictionary()
    file.seek(0)
    end = False
    output = ''
    while not end:
        c = file.read(1)
        if c == '':
            end = True
        else:
            output += str(dictionary[c])
    print(output)
    return output


def alt_encode_helper():
    input_filename = str(input("Input: "))
    output_filename = str(input("Output: "))
    input_file = read_file(input_filename)
    content = alt_encode(input_file)
    write_file(output_filename, content)


if __name__ == "__main__":
    try:
        alt_encode_helper()
    except KeyboardInterrupt:
        print()

