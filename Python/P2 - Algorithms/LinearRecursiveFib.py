__author__ = 'HaoBin'


def fib(x,y,n):
    if n <= 1:
        return y
    else:
        return fib(y,x+y,n-1)


if __name__ == "__main__":
    print(fib(0,1,6))