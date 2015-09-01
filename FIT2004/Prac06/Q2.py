__author__ = 'HaoBin'

from Q1 import *
from Q2_HashTable import *

def lexico_mergesort(array):
    # Merge sort implementation, sorts words into lexicographic order
    if len(array) <= 1:
        # if one item, consider already sorted
        return array
    else:
        # split left and right
        l = lexico_mergesort(array[0:int(len(array)/2)])
        r = lexico_mergesort(array[int(len(array)/2):])
        array = []

        # making sure len(r) is greater than len(l)
        if len(r) < len(l):
            r, l = l, r

        i = j = 0
        # loop through characters and compare them
        while i < len(l) and j < len(r):
            c = 0
            flag = False
            # ensuring character counter is less than length
            while (flag is False) and (c < len(l[i][0]) and c < len(r[j][0])):
                # l[i] is the [word, freq] pair
                # l[i][0] is the word
                # l[i][0][c] is the character
                # comparison starts
                if l[i][0][c] < r[j][0][c]:
                    array.append(l[i])
                    flag = True
                    i += 1
                elif l[i][0][c] > r[j][0][c]:
                    array.append(r[j])
                    flag = True
                    j += 1
                else:
                    # if comparison is equal, take the shorter length one
                    c += 1
                    if c == len(l[i][0]):
                        array.append(l[i])
                        i += 1
                        flag = True
                    elif c == len(r[j][0]):
                        array.append(r[j])
                        j += 1
                        flag = True

        # put remaining items in
        while i < len(l):
            array.append(l[i])
            i += 1

        while j < len(r):
            array.append(r[j])
            j += 1

        return array


def keyword_freq():
    print("Starting...")
    # Reads the file and loads them into memory for processing later
    file = open("splitwords.txt").read().split("\n")

    # Initialising the hash table and counts the frequency
    htab = HashTable()
    for line in file:
        if line != '':
            htab.insert(line)


    print("Initialising array...")
    # a = []
    # prev = ""
    # for line in file:
    #     if line != "" and line != prev:
    #         inner = [line, htab.lookup_freq(line)]
    #         a.append(inner)
    #     prev = line
    a = htab.arraylist()
    a = lexico_mergesort(a)

    print("Writing file...")
    write_file("keyword-frequency.txt","")
    for x in a:
        string = x[0].lstrip('\'').rstrip('\'') + " " + str(x[1]) + "\n"
        append_file("keyword-frequency.txt", string)

    print("keyword-frequency.txt written.")

if __name__ == "__main__":
    keyword_freq()