__author__ = 'HaoBin'

from Week5.Q6 import *

def Hirschberg(p, q, p1, p2, q1, q2):
    print(">>>",p[p1:p2],p1,p2)
    print(">>>",q[q1:q2],q1,q2)
    z = ""
    w = ""
    if p2 <= p1:
        # BASE CASE: P empty
        for i in range(q1, q2):
            z += "-"
            w += q[i]
        print("c1",z,w)

    elif q2 <= q1:
        # BASE CASE: Q empty
        for i in range(p1, p2):
            z += p[i]
            w += "-"
        print("c2",z,w)

    elif p2 - 1 == p1 or q2-1 == q1:
        # BASE CASE: LEN(P)=1 and LEN(Q)>=1
        z,w = NeedlemanWunsch(p[p1:p2],q[q1:q2])
        print("c3",z,w)


    else:
        print("l1")
        mid = (p1 + p2) // 2
        fwd = DPA(p1, mid, q1, q2, p, q)
        rev = DPA(p2, mid, q1, q2, p, q)

        s2mid = q1
        best = len(p) + len(q)
        for i in range(1,q2 - q1):
            sum = fwd[i] + rev[i]
            if sum <= best:
                best = sum
                s2mid = i
        print("r1")
        z1, w1 = Hirschberg(p, q, p1, mid, q1, s2mid)
        print("r2")
        z2, w2 = Hirschberg(p, q, mid, p2, s2mid, q2)
        z = z + z1 + z2
        w = w + w1 + w2
        print("x",z,w)
    return z, w


def DPA(p1, p2, q1, q2, p, q):
    m = [[None for i in range(len(q) + 1)] for j in range(2)]
    flag = False
    # print(p1,p2)
    if p2 < p1:
        q = q[::-1]
        p = p[::-1]
        p1, p2 = 0, p1 - p2
        flag = True
    c = p1 % 2
    m[c][q1] = 0
    for j in range(q1 + 1, q2 + 1):
        m[c][j] = m[c][j - 1] + 1
    for i in range(p1 + 1, p2 + 1):
        m[i % 2][q1] = m[(i - 1) % 2][q1] + 1
        for j in range(q1 + 1, q2 + 1):
            diag = m[(i - 1) % 2][j - 1]
            if p[i - 1] != q[j - 1]:
                diag += 2
            m[i % 2][j] = min(diag, m[(i - 1) % 2][j] + 1, m[i % 2][j - 1] + 1)
    #print(">",m)
    if flag is True:
        return m[(p2 - p1) % 2][q2 + 1:q1:-1][::-1]
    else:
        return m[(p2 - p1) % 2][q1 + 1:q2 + 1]
