__author__ = 'HaoBin'

import time, cProfile

def radix_sort_char(lst):
    for i in range(7):
        buckets = [[] for i in range(2**7)]
        j = 7-i-1
        for c in lst:
            if ord(c) >= 36:
                k = '{:07b}'.format(ord(c))[j]
                buckets[int(k,2)].append(c)
            else:
                k = '{:07b}'.format(37)[j]
                buckets[int(k,2)].append(c)
        lst = []
        for bucket in buckets:
            lst.extend(bucket)
    return lst

def bwt_preprocess(bwt_l):
    # Calculate total frequency and nOccurrences shortcut table
    freq_table = {}
    occurrence = []
    for i in range(len(bwt_l)):
        symbol = bwt_l[i]
        try:
            freq_table[symbol] += 1
        except KeyError:
            freq_table[symbol] = 0
        occurrence += [freq_table[symbol]]

    # Adjust the Frequency table to be inclusive by +1
    symbol_list = radix_sort_char(list(freq_table.keys()))[1:]
    freq_table['$'] += 1
    for symbol in symbol_list:
            freq_table[symbol] += 1

    # Calculates Rank
    rank_table = {'$':0}
    prev_rank = 0
    prev_freq = 1
    for symbol in symbol_list:
        try:
            rank_table[symbol]
        except KeyError:
            rank_table[symbol] = prev_rank + prev_freq
            prev_rank = rank_table[symbol]
            prev_freq = freq_table[symbol]

    # Calculate F
    # F = '$'
    # for i in range(len(symbol_list)):
    #     current = [symbol_list[i]] * freq_table[symbol_list[i]]
    #     F += ''.join(current)

    # Occurrence takes n space
    # Rank Table takes m space where m is equal to unique symbols
    # F takes n space
    return occurrence, rank_table

def bwt_invert_lf(L):
    init_time = time.time()
    print("Preprocessing...")
    occurrences, ranks = bwt_preprocess(L)
    print("Time taken", time.time() - init_time)

    init_time = time.time()
    print("Reconstructing...")
    final =  "$"
    finale = ""
    i = 0
    pos = 0
    # pos should start from position of $
    for k in range(len(L)):
        final = str(L[pos]) + final
        pos = ranks[L[i]] + occurrences[i]
        if L[pos] == "$":
             break
        i = pos
        if k % 50000 == 0:
             print("Processing "+ str(k) + " : " + str(pos), end="\r")
             finale = final + finale
             final = ""

    # Finale takes n space
    # Final takes auxiliary n space
    finale = final + finale
    print("Time taken", time.time() - init_time)
    return finale


def main():
    string = open("cipher.txt",'r').read()
    #string = open("bwt1000001.txt",'r').read()
    #string = open("something.txt",'r').read()
    #file = open(str(input("Filename: ")),'r')

    inverted = bwt_invert_lf(string)
    print(inverted)

    print("Writing...")
    x = open("originalstring.txt",'w').write(inverted)
    print("Done.")


if __name__ == "__main__":
    cProfile.run('main()')