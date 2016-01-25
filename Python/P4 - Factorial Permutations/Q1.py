__author__ = 'HaoBin 25461257'

import sys, time

# Time taken when N=10: ~75 seconds

def list_factorial(n):
    # generate a list of factorials up to n
    # storing each n! into a list and returns the list
    # Complexity: Best/Worst: O(n) where n is the number of factorials wanted
    f_list = [1]
    for i in range(1,n+1):
        f_list.append(i * f_list[i-1])
    return f_list

def permute(n):
    # This program at each i up to N!:
    # - Convert each i from base-10 to base-!
    # - Convert base-! into a permutation string based on sorted alphabetical total order
    # - Compute sum of the base-! digits
    # - Prints out the result to a file
    # Complexity: O(N!) where N! is the number of total permutations

    # generating factorials
    f_list = list_factorial(n)

    # print("Converting to base-!...")
    f_nums = permute_conversion(n, f_list)

    # generating a total ordering based on sorted order of the alphabets
    total_ordering = []
    for i in range(n):
        total_ordering.append(str(chr(97 + i)))

    permutation_strings = []
    # print("Converting base-! to permutation strings...")
    for i in range(f_list[n]):
        permutation_strings.append(permute_fac_to_str(f_nums[i], total_ordering))

    # print("Conversion complete, printing results...")
    print_permute(n, f_list[n], f_nums, permutation_strings)


def permute_fac_to_str(f_num, total_ordering):
    # Converts a base-! number into a string based on total ordering
    # Complexity: O(n) where n is the length of each permute string
    total_ordering = total_ordering[:]
    permutation_str = []
    for i in range(len(f_num)):
        permutation_str.append(total_ordering[f_num[i]])
        del total_ordering[f_num[i]]
    return permutation_str

def permute_conversion(n, f_list):
    # Complexity: O(n!), where n! is the number of total permutations
    # converts n into base-!
    results = []
    for i in range(f_list[n]):
        results.append(permute_conversion_num(i, f_list, n))
    return results

def permute_conversion_num(i, f_list, n):
    # Complexity: O(n) where n is the length of each permutation string
    # does the heavy work of converting i into base-!
    list = [0] * n
    x = i
    for j in range(n):
        list[j] = x // f_list[n-1-j]
        x -= (list[j] * f_list[n-1-j])
    return list

def print_permute(n, n_fac, f_nums, permutation_strings):
    # Complexity: O(N!) where N! is the number of total permutations
    # prints out the results to a file in a specified format
    oldstdout = sys.stdout
    filename = "fit2004_lab4_output" + str(time.time()) + ".txt"
    log = open(filename, "w")
    sys.stdout = log

    print("INPUT TO THE SCRIPT: N = " + str(n))
    print("TOTAL NUMBER OF PERMUTATIONS = " + str(n_fac))
    print("decimal".ljust(20, " ") + "factoradic".ljust(18, " ") + "sum".center(10, " ") + "permutation".center(30, " "))
    frequency_list = [0] * ( sum(f_nums[len(f_nums)-1]) + 1 )
    for i in range(n_fac):
        decimal = "(" + str(i).rjust(10) + str(")_10")
        decimal = decimal.ljust(20, " ")

        factoradic = "(" + "".join([str(j) for j in f_nums[i]]) + ")_!"
        factoradic = factoradic.ljust(18, " ")

        f_sum = sum(f_nums[i])
        frequency_list[f_sum] += 1
        sum_ = str(f_sum).center(10, " ")

        permutation = "".join(permutation_strings[i])
        permutation = permutation.center(30, " ")

        print(decimal + factoradic + sum_ + permutation)

    print("\nFREQUENCY TABLE")
    print("-" * 15)
    print("SUM".center(7) + "FREQ.".center(8))
    weighted_sum = 0
    for i in range(len(frequency_list)):
        weighted_sum += i*frequency_list[i]
        print(str(i).center(7) + str(frequency_list[i]).center(7))
    sys.stdout = oldstdout
    print("Weighted average of sum = " + str(weighted_sum/sum(frequency_list)))

    sys.stdout = oldstdout
    print("Results printed.")

if __name__ == "__main__":
    n = int(input("N = "))
    permute(n)

"""
Question 1(d)
The weighted average is growing asymptotically as a function of N at the rate of (N^2).

MAX = N(N-1)/2
F(N) = (Freq(0) * 0 + Freq(1)*1 + ... + Freq(Max) * Max) / n!
And notice Freq(0) = Freq(Max), Freq(1) = Freq(Max-1), ...

If MAX even: e.g n=4
Notice 0*1 + 1*3 + 2*5 + 3*6 + 4*5 + 5*3 + 6*1
Can be simplified to 6*1 + 6*3 + 6*5 + 3*6
F(N) = ( MAX * ( Freq(0)+...+Freq(MAX/2 - 1) ) + MAX/2*(Freq(max/2) ) / n!
F(N) = [ N(N-1)/2 * ( N!/2 - Freq(N/2)/2 ) + ( n(n-1)/4 * freq(n/2) ) ] / n!
F(N) = n(n-1)/4 [ (n! - freq(n/2) + Freq(n/2)) ] / n!
F(N) = N(N-1)/2 * (n!/2) / n!
F(N) = (N(N-1) * N!) / 4N!
F(N) = N(N-1) / 4
F(N) = (N^2 - N) / 4
>>> O(N^2)

If MAX odd: e.g n=3
Notice               >> 0*1 + 1*2 + 2*2 + 3*1
Can be simplified to >> 3*1 + 3*2
Hence,
F(N) = ( MAX * ( Freq(0)+...+Freq(MAX/2) ) / n!
F(N) = ( MAX * ( n!/2 ) / n!
F(N) = ( N(N-1)/2 * n!/2 ) / n!
F(N) = ( N(N-1) * n! ) / 4n!
F(N) = N(N-1) / 4               #simplify
F(N) = (N^2 - N) / 4
>>> O(N^2)


Question 1(e)
Insertion sort - At every step of the iteration, it takes one element from the unsorted
part of the list[i:n] and put it in the correct place in sorted part of the list[0:i].

Average case - Because the weighted average of sum, is the average of sum of "frequency
of each minimum adjacent swaps needed to achieve sorted order" multiplied by
the "minimum adjacent swaps needed to achieve sorted order". Hence when given
N = 4, weighted average of sum = 3, it means: it takes an average of 3 minimum swaps
in order to sort a list with 4 elements using insertion sort.
"""

