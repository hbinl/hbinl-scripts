__author__ = 'HaoBin'

import cProfile

def rbk(pat,txt):
    n = len(txt)
    m = len(pat)
    h_pat = rolling_hash(pat)
    h_txt = rolling_hash(txt[0:m])

    for i in range(n-m+1):
        if h_pat == h_txt:

            for j in range(m):
                match = True
                if txt[i+j] != pat[j]:
                    match = False
                if match is True:
                    return i
        h_txt = update_rolling_hash(h_txt, txt[i:i+m+1])
    return -1

def rolling_hash(string,d=131):
    q = 32452843
    hash = ord(string[0]) * d + ord(string[1])
    for i in range(2,len(string)):
        hash = hash * d + ord(string[i])
    return hash % q

def update_rolling_hash(hash,txt,d=131):
    q = 32452843
    h = (hash - (ord(txt[0]) * (d**(len(txt)-2))) ) * d + ord(txt[len(txt)-1])
    return h % q


def main():
    file = open("9-patterns.txt","r")
    t = []
    for line in file:
        t.append(line.strip())
    print()
    # for pat in t:
    #     count = 0
    k = 0
    for pat in t:
        for txt in t:
            o = rbk(txt,pat)
            if o != 0:
                k += o
        print(pat,k)
        k = 0


if __name__ == "__main__":
    cProfile.run('main()')
