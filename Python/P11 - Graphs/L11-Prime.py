__author__ = 'HaoBin'

import random


def FermatRandomizedTest(n):
    a = random.randint(1,n-1)
    if (a**(n-1)) % n != 1:
        print("Composite!")
        return
    print("Probably Prime!")


def miller_rabin(n,k=128):
    # TO ASK
    if n%2==0:
        print("Composite")
        return

    s=0
    t=n-1
    while t%2==0:
        s += 1
        t = t//2

    print(n-1,(2**s)*t,s,t)

    for _ in range(k):
        a = random.randint(2,n-2)
        if (a**(n-1)) % n != 1:
            print("Composite2")
            return
        for i in range(1,s-1):
            p1 = a**((2**(i)) * t)
            p2 = a**((2**(i-1)) * t)
            print(a,i,p1,p2)
            if (p1 % n) == 1 and ((p2 % n != 1) or (p2%n != n-1)):
                print("Composite4")
                return
    print("Probably Prime")

def miller_rabin_2(n,k=1000):
    if n%2==0:
        print("Composite")
        return

    s=0
    t=n-1
    while t%2==0:
        s += 1
        t = t//2


    for _ in range(k):
        do_next = False
        a = random.randint(2,n-2)
        x = (a**t) % n
        if x == 1 or x == n-1:
            pass
            do_next = True
        else:
            for i in range(s-1):
                x = x**2 % n
                if x == 1 :
                    print("Composite")
                    return
                if x == n-1:
                    do_next = True
                    break
        if do_next == False:
            print("Composite")
            return
    print("Probably Prime")


if __name__ == "__main__":
    miller_rabin(17)
    # for n in range(4,100):
    #     print(n)
    #     FermatRandomizedTest(n)
    #     miller_rabin(n)
    #     miller_rabin_2(n)
    #     print()