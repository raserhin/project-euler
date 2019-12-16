"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""
# TODO: This solution could be optimized

from sympy import primefactors


N = 1_000_000
len_factors = 4
numbers = (i for i in range(1, N) if len(primefactors(i)) == len_factors)
found = []
for number in numbers:
    if not found or number - found[len(found) - 1]   == 1:
        found.append(number)
    else:
        found = [number]

    if len(found) == len_factors:
        print(found[0])
        break
