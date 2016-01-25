__author__ = 'HaoBin'




def x():
    for i in range(100):
        z = i+1
        if z%3 == 0 and z%5 == 0:
            print("FizzBuzz")
        elif z%3==0:
            print("Fizz")
        elif z%5==0:
            print("Buzz")
        else:
            print(z)


def y():
    for i in range(1, 101):
        z = ""
        z = z + "Fizz" if i % 3 == 0 else z
        z = z + "Buzz" if i % 5 == 0 else z
        print(z) if z != "" else print(i)

y()