__author__ = 'HaoBin 25461257'

from Q1 import *


def permute_alt(n, total_ordering):
    # Complexity: O(N!) where N! is the number of total permutations
    # works generally the same as permute(), except total ordering now depends
    # on the second permutation that you want to convert to.
    # Basically second permutation is now considered the "sorted" base case.
    f_list = list_factorial(n)
    f_nums = permute_conversion(n, f_list)
    total_ordering = list(total_ordering)

    # generate list of permutation strings
    permutation_strings = []
    for i in range(f_list[n]):
        permutation_strings.append(permute_fac_to_str(f_nums[i], total_ordering))
    print_permute(n, f_list[n], f_nums, permutation_strings)


def smallest_transposition(p1, p2):
    if len(p1) != len(p2):
        # the permutation strings must be same length
        raise ValueError("Must be same length.")

    # convert the input strings into lists
    initial = list(p1)
    total_ordering = list(p2)

    # reversing the string into its base-! according to the total ordering
    factoradic = str_to_factoradic(initial, total_ordering)

    print("The smallest number of adjacent transposition: " + str(sum(factoradic)))


def str_to_factoradic(str, total_ordering):
    # Complexity: O(N) where n is the length of the permute string
    # a reverse function for converting string back into its base-!
    # based on the current total ordering
    factoradic = []
    for i in range(len(str)):
        x = total_ordering.index(str[i])
        factoradic.append(x)
        del total_ordering[x]
    return factoradic


if __name__ == "__main__":
    p1 = str(input("P1 = "))
    p2 = str(input("P2 = "))
    smallest_transposition(p1, p2)
    print("\nPrinting total results.")
    n = len(p2)
    permute_alt(n, p2)