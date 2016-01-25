__author__ = 'HaoBin'

import cProfile, math


def primegen_era(limit):
    # Sieve of Erathosthenes

    # Complexity: O(n log(log n))
    # Inner loop does n/i iterations (becuz ++ steps of i)
    # sum of all the inner loop sequences = sum(N/i) where N is a constant
    # hence, sum(N/i) = N * sum(1/i)
    # Prime Harmonic series sum: 1/i = log(log n)
    # hence O(N * log(log n))

    print("Initialising...", end='\r')

    lst = [True] * limit

    if limit >= 4:
        for i in range(4,limit,2):
            lst[i] = False

    for i in range(3, int(math.sqrt(limit))+1):
        if lst[i] is True:
            j = i*i
            while j < limit:
                lst[j] = False
                j += i
        print(i, end='\r')


    prime_lst = []
    for i in range(2,len(lst)):
        if lst[i] is True:
            prime_lst.append(i)
    print("Sieve of Erathosthenes done.")


    p_list = prime_lst[-100:][::-1]

    print("Largest 100 Primes:", p_list)

    c_list = [x-1 for x in p_list]

    print("Composites (P-1):", c_list)

    #c_list = [25852]

    # START FACTORISATION
    print("\nFactorisations:")
    for c in c_list:
        factorisation = []
        n = c
        p_idx = 0
        for i in range(len(prime_lst)):
            if n % prime_lst[p_idx] == 0:
                factorisation.append(prime_lst[p_idx])
                n = n // prime_lst[p_idx]

                if n <= prime_lst[p_idx] and n % prime_lst[p_idx] != 0:
                    break
            else:
                p_idx += 1

        print(c,"=", "*".join(str(factor) for factor in factorisation))

    print()


def main():
    # lim is exclusive
    lim = 100000000
    primegen_era(lim)

if __name__ == "__main__":
    #main()
    cProfile.run("main()")