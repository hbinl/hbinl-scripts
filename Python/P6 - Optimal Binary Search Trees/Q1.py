__author__ = 'HaoBin'

def read_file(filename):
    file = open(filename, 'r')
    return file

def write_file(filename, content):
    file = open(filename, 'w')
    file.write(content)
    file.close()
    return True

def append_file(filename, content):
    file = open(filename, 'a')
    file.write(content)
    file.close()
    return True

def process(file):
    # Reads the file one character at a time and convert them to all uppercase
    # and eliminate symbols
    # Returns a list of separate words
    # Complexity O(N)
    file.seek(0)
    final = ""
    while True:
        c = file.read(1)
        if c == "":
            break
        else:
            asc = ord(c)
            if 97 <= asc <= 122:
                final += chr(asc - 32)
            elif 65 <= asc <= 90 or asc == 32:
                final += chr(asc)
            else:
                final += chr(32)
    return final.split(" ")


def split_words():
    # Time complexity: O(n) where N is the number of characters/lines
    filename = str(input("Open filename: "))
    file = read_file(filename)

    # Starts the processing and splitting process
    # Returns a list with words, which were separated by spaces
    print("Processing...")
    final = process(file)

    # For each word in the list, write into file + next line
    print("Writing file...")
    write_file("splitwords.txt", "")
    for word in final:
        if len(word) > 1:
            append_file("splitwords.txt", str(word) + "\n")

    print("splitwords.txt written.")

if __name__ == "__main__":
    split_words()