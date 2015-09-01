__author__ = 'HaoBin'

import random
import time

def smooth_buggy(list, w):
    if w % 2 == 0 or w < 0:
        raise ValueError("w must be odd and positive")
    smoothed_list = []
    x = w // 2
    for i in range(len(list)):
        sum = 0
        if i-x < 0:
            sum = (x-i) * list[0] + list[i]
            c = i+x+1
            if c > len(list):
                c = len(list)
            for j in range(1, c):
                sum += list[j]
        elif i >= len(list) - x:
            sum = x * list[len(list) - 1] + list[i]
            c = i-x
            if c < 0:
                c = 0
            for j in range(c, i):
                sum += list[j]
        else:
            for j in range(i-x, i+x+1):
                sum += list[j]
        smoothed_list.append(sum / w)
    return smoothed_list

def smooth_alt(list,w):
    if w % 2 == 0 or w < 0:
        raise ValueError("w must be odd and positive")
    smoothed_list = []
    x = w // 2
    for j in range(len(list)):
        i = 0
        sum = 0
        while i < w:
            c = j + x - i
            if c < 0:
                c = 0
            elif c > len(list) - 1:
                c = len(list) - 1
            sum += list[c]
            i += 1
        sum = sum / w
        smoothed_list.append(sum)
    return smoothed_list

def smooth_optimised_cheatwindow(list, w):
    if w % 2 == 0 or w < 0:
        raise ValueError("w must be odd and positive")
    x = w // 2
    smoothed_list = []
    for i in range(x):
        list = [list[0]] + list
        list.append(list[len(list)-1])
    z = sum(list[0:w])
    smoothed_list.append(z/w)

    j = 0
    for i in range(x+1, len(list)-x):
        z = z - list[j] + list[i+x]
        smoothed_list.append(z/w)
        j += 1

    return smoothed_list

def smooth_optimised(list, w):
    if w % 2 == 0 or w < 0:
        raise ValueError("w must be odd and positive")
    x = w // 2
    smoothed_list = []
    z = sum(list[0:x+1]) + (x * list[0])
    #print(z)
    smoothed_list.append(z/w)

    for i in range(1, len(list)):
        j = i+x
        if j > len(list)-1:
            j = len(list)-1

        k = i-x-1
        if k < 0:
            k = 0

        if i-x <= 0:
            z = z - list[0] + list[j]
        elif i+x >= len(list)-1:
            z = z - list[k] + list[len(list)-1]
        else:
            z = z - list[k] + list[j]

        smoothed_list.append(z/w)

    return smoothed_list


def smooth_x(list, w):
    if w % 2 == 0 or w < 0:
        raise ValueError("w must be odd and positive")
    extension = (w-1) // 2
    front = [list[0]] * extension
    back = [list[len(list)-1]] * extension
    list = front + list + back

    sum_x = 0
    smoothed = []
    for i in range(w):
        sum_x += list[i]

    smoothed.append(sum_x/w)

    for i in range(w-1, len(list)-1):
        sum_x = sum_x + list[i+1] - list[i-w+1]
        smoothed.append(sum_x/w)

    #print(smoothed)


if __name__ == "__main__":
    list = [2.0, 5.0, 5.0, 8.0, 2.0, 2.0, 5.0]
    list = []
    for i in range(100000):
        list.append(random.uniform(0,10))
    #print(list)
    w = int(input("w = "))

    print("New")
    start = time.time()
    smooth_x(list, w)
    print((time.time() - start) * 1000000)

    # print("buggy version?")
    # start = time.time()
    # smoothed = smooth_buggy(list, w)
    # print((time.time() - start) * 1000000)
    # print(smoothed)

    print("\n Correct but unoptimised version?")
    start = time.time()
    smoothed = smooth_alt(list, w)
    print((time.time() - start) * 1000000)
    #print(smoothed)

    #
    # print("\n Optimised version with a cheating window")
    # start = time.time()
    # smoothed = smooth_optimised_cheatwindow(list, w)
    # print((time.time() - start) * 1000000)
    # #print(smoothed)

    print("\n Optimised version")
    start = time.time()
    smoothed = smooth_optimised(list, w)
    print((time.time() - start) * 1000000)
    #print(smoothed)