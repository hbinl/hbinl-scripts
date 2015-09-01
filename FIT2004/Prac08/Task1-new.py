__author__ = 'HaoBin'

import time, cProfile

def encode_kmer(kmer):
    # Takes a string, and converts it to a single
    # binary string based on base-4 encoding.
    # A - 0/00, C - 1/01, G - 2/10, T - 3/11
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    dict = {'A':'00', 'C': '01', 'G':'10', 'T':'11'}
    strg = []
    for i in range(len(kmer)):
        strg.extend([str(dict[kmer[i]])])
    return ''.join(strg)

def keypair_radix(lst):
    # Radix sort for a list of key-value pairs
    # Time Complexity: O(n)
    # Space Complexity: O(n) auxillary
    for i in range(4):
        buckets = [[] for i in range(2**8)]
        j = 8*(4-i) - 8
        for pair in lst:
            k = pair[0][j:j+8]
            buckets[int(k,2)].append(pair)
        lst = []
        for bucket in buckets:
            lst.extend(bucket)
    return lst

def main():
    init_time = time.time()
    file = open("longstring.txt", 'r')
    print("Initialising 16-mers...")
    i = 0
    file.seek(0)
    lst = []
    decode_list = []
    kmer = file.read(16)
    lst.append((encode_kmer(kmer), i))
    decode_list.append(kmer)

    while True:
        new_char = file.read(1)
        if new_char == "\n":
            break
        new_kmer = lst[i][0][2:] + str(encode_kmer(new_char))
        i += 1
        lst.append((new_kmer, i))
        decode_list.append(str(decode_list[i-1][1:]) + str(new_char))
    print("t: " + str((time.time() - init_time)))

    init_time = time.time()
    print("Sorting...")
    lst = keypair_radix(lst)
    print("t: " + str((time.time() - init_time)))

    init_time = time.time()
    print("Writing sorted16mers.txt...")
    open("sorted16mers.txt", 'w').close()
    file = open("sorted16mers.txt", 'a')
    for pair in lst:
        file.write(str(decode_list[pair[1]]) + " " + str(pair[1]) + "\n")
    print("t: " + str((time.time() - init_time)))

if __name__ == "__main__":
    cProfile.run('main()')