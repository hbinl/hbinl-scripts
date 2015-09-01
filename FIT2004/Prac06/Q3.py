__author__ = 'HaoBin'

from Q1 import *
import sys, time

def min_cost_bst(t):
    # Complexity: Average O(n^2), Worst O(n^3) - look at w and r matrix part

    cdt = time.time()               # countdown timer
    n = len(t)+1                    # n for computing matrix calculations
    array_sizes = int(n*(n+1)/2)    # calculate appropriate array size for triangular matrices

    print("Allocating arrays...")
    w = [None] * array_sizes  # 1D array for storing minimum costs/weights
    p = [None] * array_sizes  # 1D array for storing probabilities
    r = [None] * array_sizes  # 1D array for storing the nodes/roots

    print("Initialising arrays...")
    # initialise the diagonal zeroes and diagonal+1 values
    for i in range(n):
        for j in range(n):
            k = trimatrix_translate(i,j,n)
            if i == j:
                w[k] = 0
                p[k] = 0
                r[k] = 0
            if j == i+1:
                r[k] = j
                w[k] = p[k] = t[i][1]

    print("Initialising p matrix...")
    for i in range(n):
        for j in range(i+2,n):
            k = trimatrix_translate(i,j,n)
            arg_1 = trimatrix_translate(i,j-1,n)
            arg_2 = trimatrix_translate(j-1,j,n)
            p[k] = p[arg_1] + p[arg_2]

    print("Initialising w and r matrix...")
    for j in range(2,n):
        c = 0
        for i in range(0,n-2):
            k = trimatrix_translate(i, j+c, n)
            if w[k] is not None:
                break
            minima, min_k = get_min(w,i,j+c,n,r)
            r[k] = min_k
            w[k] = p[k] + minima
            c +=1

    print("Writing output...")
    open("mincostbst.txt", "w").close()
    oldstdout = sys.stdout
    log = open("mincostbst.txt", "a")
    sys.stdout = log

    sum = 0
    for i in range(len(t)):
        k = trimatrix_translate(i,i+1,n)
        level = matrix_tree_traverse(r, n, i+1, 0, n-1)
        sum += w[k] * level
        print(str(t[i][0]).rjust(15), str(t[i][2]).rjust(6), str(level).rjust(6), str(format(sum,".6f")).rjust(10))
    sys.stdout = oldstdout

    print("mincostbst.txt written. Time taken:", int(time.time() - cdt), "s" )

    # Optional, output the matrix into a file for debugging purposes
    # print("Extra: Writing matrices file... ")
    # open("mincostbst-matrices.txt", "w").close()
    # trimatrix_print(w,n)
    # trimatrix_print(p,n)
    # trimatrix_print(r,n)


def matrix_tree_traverse(r, n, key, i, j):
    # traverse the matrix R as if it is a binary tree
    # r - matrix R
    # n - dimension of matrix
    # key - the item in search
    # i,j - starting coordinates
    # complexity: Worse case O(n), Best Case O(log n)

    c = trimatrix_translate(i, j, n)
    if i < j:
        if r[c] is None or r[c] == 0.0:
            return 0
        elif r[c] == key:
            return 1
        else:

            m = r[c]
            next_possible_subtree = [[i,m-1],[m,j]]
            level = 0
            for subtree in next_possible_subtree:
                level = matrix_tree_traverse(r,n,key,subtree[0],subtree[1])
                if level != 0:
                    level += 1
                    break
            return level
    else:
        return 0


def get_min(w,i,j,n,r):
    array = []
    idx_1 = trimatrix_translate(i+1,j,n)
    idx_2 = trimatrix_translate(i,j-1,n)

    # Unused : Slow version
    # for c in range(r[idx_1]- r[idx_2]+1):
    #     k = i + c + 1
    #     arg_1 = trimatrix_translate(i,k-1,n)
    #     arg_2 = trimatrix_translate(k,j,n)
    #     print(i,k-1,"+",k,j)
    #     if arg_2 >= len(w):
    #         break
    #     array.append([w[arg_1] + w[arg_2], k])

    # Inner find_min loop
    # Optimisation based on Knuth's observations that R[i,j-1] < R[i,j] < R[i+1,j]
    # So we only have to look for range from R[i,j-1] to R[i+1,j]
    # Making the whole algorithm of this program - average O(N^2)
    for k in range(r[idx_2], r[idx_1]+1):
        arg_1 = trimatrix_translate(i,k-1,n)
        arg_2 = trimatrix_translate(k,j,n)
        if arg_2 >= len(w):
            break
        array.append([w[arg_1] + w[arg_2], k])

    minimum = min(array, key = lambda x: x[0])
    return minimum[0], minimum[1]


def trimatrix_translate(i,j,n):
    # (i*n)+j transforms i,j coordinates of a matrix of nxn size
    # into 2d array indexes
    # -(i*(i+1))/2 deducts the corresponding ignored cells
    # for triangular matrices
    return int((i * n) + j - (i*(i+1)) / 2)

def trimatrix_print(m,n):
    # A function for printing the triangular matrices into a file for easy viewing
    oldstdout = sys.stdout
    filename = "mincostbst-matrices.txt"
    log = open(filename, "a")
    sys.stdout = log
    idx = 0
    grid_size = 12
    for row in range(n):
        print()
        for i in range(row):
            print("".rjust(grid_size), end="")
        for k in range(n-row):
            print(str(   format(m[idx],".4f")    ).rjust(grid_size),end="")
            idx += 1
    print()
    sys.stdout = oldstdout

def mcbst_main():
    print("Starting...")
    file = open("keyword-frequency.txt")
    splitted = file.read().split("\n")
    array = []
    for line in splitted:
        if line != "":
            array.append(line.split())

    total_frequency = 0
    for word in array:
        total_frequency += int(word[1])

    for word in array:
        word.append(word[1])
        word[1] = (int(word[1]) / total_frequency)

    min_cost_bst(array)


if __name__ == "__main__":
    try:
        mcbst_main()

    except KeyboardInterrupt:
        pass
