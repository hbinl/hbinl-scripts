__author__ = 'HaoBin'

def factorial_recursive(n):
    # O(n) complexity
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

if __name__ == "__main__":
    try:
        n = int(input("Please input a number to calculate factorial: "))
        print(factorial_recursive(n))
    except ValueError:
        print("Invalid number input.")



