__author__ = 'HaoBin'

from Week5.Q6 import *

def HirschbergA(x,y):
    # print(x,y)
    xa = ""
    ya = ""
    if len(x) == 0:
        for i in range(1,len(y)):
            xa += "-"
            ya += y[i]
    elif len(y) == 0:
        for i in range(1,len(x)):
            xa += x[i]
            ya += "-"
    elif len(x) == 1 or len(y) == 1:
        # BASE CASE: LEN(P)=1 and LEN(Q)>=1
        xa,ya = NeedlemanWunsch(x,y)
    else:
        xlen = len(x)
        ylen = len(y)
        xmid = len(x) // 2

        fwd = xDPA(x[0:xmid],y)
        rev = xDPA(x[xmid:xlen][::-1], y[::-1])
        rev = rev[::-1]
        # print(fwd)
        # print(rev)

        ymid = 0
        best = float("inf")
        for i in range(1,len(y)+1):
            sum = fwd[i] + rev[i]
            if sum < best:
                best = sum
                ymid = i
        z1, w1 = HirschbergA(x[0:xmid],y[0:ymid])
        z2, w2 = HirschbergA(x[xmid:xlen],y[ymid:ylen])
        xa = xa + z1 + z2
        ya = ya + w1 + w2
    print(xa,ya)
    return xa,ya



def xDPA(x,y):
    m = [[None for i in range(len(y)+1)] for j in range(2)]
    m[0][0] = 0
    for j in range(1,len(y)+1):
        m[0][j] = m[0][j-1] + 1
    for i in range(1, len(x)+1):
        m[i %2][0] = m[(i-1)%2][0] + 1
        for j in range(1, len(y)+1):
            diag = m[(i - 1) % 2][j - 1]
            if x[i - 1] != y[j - 1]:
                diag += 1
            m[i % 2][j] = min(diag, m[(i - 1) % 2][j] + 1, m[i % 2][j - 1] + 1)
    # for n in range(len(m)):
    #     print(m[n])

    return m[i%2]


def main():

    # s1 = "ABCD"
    # s2 = "CBA"
    #
    # s1 = "DENTIST"
    # s2 = "DENTEST"
    # s1 = "ABCD"
    # s2 = "CBDA"
    # s1="INTENTION"
    # s2="EXECUTION"
    # s1 = "DIRTYROOM"
    # s2 = "DORMITORY"
    # s1 = "AGTA"
    # s2 = "TATGC"
    s1 = "ACTACCTACAGT"
    s2 = "ACGTACGTACGT"
    # s1 = "ACGTACGTACGT"
    # s2 = "AGTACCTACCGT"
    # s1 = "DNASGIVETHIS"
    # s2 = "DENTSGNAWSTRIMS"



    #print(xDPA("AGTA","TATGC"))

    z,w = HirschbergA(s1,s2)
    print("\nHirschberg")
    print(z)
    print(w)
    print("\nNeedleman")
    z,w = NeedlemanWunsch(s1,s2)
    print(z)
    print(w)
    # z,w = Hirschberg(p, q, 0, len(p), 0, len(q))
    # print(z)
    # print(w)

    # p = "C"
    # q = "A"
    # DPEditDistance(p,q)


if __name__ == "__main__":
    main()