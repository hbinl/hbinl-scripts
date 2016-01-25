__author__ = 'HaoBin'

import cProfile


def gray_code_gen(n):
    # based on the gray code algorithm / reflected binary code
    lst = [[0], [1]]  # 1 bit base

    for i in range(n-1):
        lst = [[0]+x for x in lst] + [[1]+x for x in lst[::-1]]

    return lst


def subset_gen(n):
    lst = gray_code_gen(n)

    total_set = []
    for i in range(n):
        total_set = [chr(65+i)] + total_set

    for combination in lst:
        subset = []
        for i in range(n-1,-1,-1):
            if combination[i] == 1:
                subset.append(total_set[i])
        print(subset)


if __name__ == "__main__":
    cProfile.run("subset_gen(5)")