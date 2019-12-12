"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations
from math import sqrt, floor


def is_prime(x, lookup_table):
    """ Determine if x is prime"""
    for prime in lookup_table:
        if x % prime ==0:
            return False
    return True
def prime_generator(N=10):
    sieve = [False, False] + [True] * N  # Added 0 and 1

    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i*i, len(sieve), i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]



"""
Being n the number of digits, it cannot be 9 neither 8.
9*10/2 = 45 # Divisible by 3
8*9/2 = 36  # Divisible by 3
"""
n = 7
lookup_prime = prime_generator(floor(sqrt(10**(n-1)) + 1))



while n > 4:
    digits = list(range(1, n+1))[::-1]

    for perm in permutations(digits, n):
        num = int("".join([str(i) for i in perm]))
        if is_prime(num, lookup_prime):
            print(num)
            n = 0
            break
    n -= 1
