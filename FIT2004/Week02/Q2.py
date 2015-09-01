__author__ = 'HaoBin'


def factorial_iterative(n):
    x = 1
    for i in range(1,n+1):
        x = i * x
    return x

if __name__ == "__main__":
    try:
        n = int(input("Please input a number to calculate factorial: "))
        print(factorial_iterative(n))
    except ValueError:
        print("Invalid number input.")
