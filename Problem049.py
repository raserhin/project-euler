"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from itertools import permutations, combinations_with_replacement


def prime_generator(N=10):
    sieve = [False, False] + [True] * N  # Added 0 and 1

    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i*i, len(sieve), i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime}


lookup_prime = prime_generator(10_000)


digits = list("9876543210")
generator = (i for i in combinations_with_replacement(digits, 4) )

for comb in generator:
    gen = list({int("".join(i)) for i in permutations(comb) if i[0] != "0" and int("".join(i)) in lookup_prime})
    if len(gen) >= 3:
        gen.sort()
        for _i, prime in enumerate(gen):
            i=_i
            while i < len(gen) - 2:
                # print(i, prime, gen[i+1], 2*gen[i+1] - prime)
                if 2*gen[i+1] - prime in gen and prime != 1487:
                    print( prime, gen[i+1], 2*gen[i+1] - prime, sep="")
                i+=1


    # 2969 6299 9629
