__author__ = 'HaoBin'


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
    #print(occurrence)
    return rank_table


def occurrence(pat, L, p):
    o = 0
    for i in range(p):
        if L[i] == pat:
            o += 1

    return o



def bwt_string_search(pat,ranks,bwt):
    sp = 0
    ep = len(bwt) - 1
    i = len(pat)
    #print(sp,ep,i)
    while i > 0:
        # print(">",occurrence(pat[i-1], bwt, sp))
        # print(">",occurrence(pat[i-1], bwt, ep+1))

        sp = ranks[pat[i-1]] + occurrence(pat[i-1],bwt,sp)
        ep = ranks[pat[i-1]] + occurrence(pat[i-1],bwt,ep+1) - 1
        i -= 1
        print(sp,ep,i)

    if ep < sp:
        multiplicity = 0
    else:
        multiplicity = ep - sp + 1

    return multiplicity

def bwt_string_search_init():
    patterns = open("9-patterns.txt", 'r')
    bwt = open("9-bwt.txt").read()
    pat_l = []
    for pat in patterns:
        pat_l.append(pat.strip())

    #bwt = "lo$oogg"

    ranks = bwt_preprocess(bwt)

    #pat_l = ["AGGAAGGA"]
    #pat_l = ["go"]

    for pat in pat_l:
        print(pat, ">>>",bwt_string_search(pat,ranks,bwt))



if __name__ == "__main__":
    bwt_string_search_init()