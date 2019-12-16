"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""
from math import sqrt, floor


def prime_generator(N=10):
    """ Creation of a set to act as a lookup table"""
    sieve = [False, False] + [True] * N  # Added 0 and 1

    for i in range(2, N+1):
        if sieve[i]:
            for j in range(i*i, N+1, i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime}


def is_composite(odd):
    return any(odd - 2*i**2 in lookup_prime for i in range(1, odd))


def odd_generator():
    """ Infinite generator for non prime odd numbers """
    current = 9  # First non prime odd number
    while True:
        if current not in lookup_prime:
            yield current
        current += 2


N = 10_000

lookup_prime = prime_generator(N=N)
for i in odd_generator():
    if not is_composite(i):
        print(i)
        break
