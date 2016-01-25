__author__ = 'HaoBin'

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def swap(a,b):
    tmp = a
    a = b
    b = tmp

    return a,b


if __name__ == "__main__":
    try:
        a = int(input("Please input first number: "))
        b = int(input("Please input second number: "))

        if a < b:
            a,b = swap(a,b)

        print(gcd(a, b))

    except ValueError:
        print("Invalid number input.")

