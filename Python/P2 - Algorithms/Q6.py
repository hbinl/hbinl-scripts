__author__ = 'HaoBin'

from Q5 import *

def fib(n):
    # Exponential complexity O(2^n)
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

########################################


def linear_fib(x,y,n):
    # Linear Recursive version
    if n <= 1:
        return y
    else:
        return linear_fib(y, x+y, n-1)


def fib_linear_iter(n):
    a = 0
    b = 1
    while n > 1:
        tmp_a = a
        a = b
        b = tmp_a + b
        n -= 1
    return b

########################################
def fast_fib(n):
    # O(log n) complexity, due to exponent by squares
    #n -= 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = [[1,1],[1,0]]
    ap = matrix_power(a,n+1)
    m = [[0], [1]]
    x = matrix_multiply(2,1,ap,m)
    return x[1][0]


def matrix_power(m, p):
    if p <= 1:
        return m
    else:
        r = matrix_power(m,p//2)
        r = matrix_multiply(len(m),len(m[0]),r,r)
        if (p % 2 == 1):
            r = matrix_multiply(len(m),len(m[0]),r,m)
        return r

################################################
#Alternative implementation of fast_fib
def alt_fib(n):
    # calculates fibonacci number in log(n) time
    if (n <= 1):
        return 1

    m = [[1, 1], [1, 0]]    #initial matrix
    r = [[1,0],[0,1]] #identity matrix
    while n > 0:
        if (n%2 == 1):
            r = matrix_multiply(2,2,r,m)
        n = n//2
        m = matrix_multiply(2,2,m,m)

    return r[1][0]

################################################


def log_fib(n):
    #print(n)
    if n <= 2:
        return 1
    else:
        if n % 2 == 1:
            k = (n + 1) // 2
            return log_fib(k) ** 2 + log_fib(k-1) ** 2
        else:
            k = n//2
            fn = log_fib(k)
            fn1 = log_fib(k-1)
            return fn * (fn + 2*fn1)

################################################

if __name__ == "__main__":
    try:
        for n in range(20):
        #n = int(input("Please input a number: "))
        #print("The " + str(n) + "th Fibonacci number is " + str(fib(n)))

            print("bin_rec", fib(n))
            # print("linear", linear_fib(0,1,n))
            # print("log",log_fib(n))
            print("fast_fib",fast_fib(n))
            print()



    except ValueError:
        print("Invalid number input.")




