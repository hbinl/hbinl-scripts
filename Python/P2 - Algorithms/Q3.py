__author__ = 'HaoBin'

import math

def prime(n):
    for i in range(1,n+1):
        flag = True
        if i == 2:
            print(i)
        elif (i == 1) or (i % 2 == 0):
            pass
        else:
            for j in range(3, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    flag = False
                    break
            if flag == True:
                print(i)

if __name__ == "__main__":
    try:
        n = int(input("Please input a number: "))
        prime(n)
    except ValueError:
        print("Invalid number input.")