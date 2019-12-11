"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt, ceil
from time import time


def prime_generator(N=10):
    sieve = [False, False] + [True] * N # Added 0 and 1 
    
    for i in range(2, N):
        if sieve[i]:
            yield i
            for j in range(i*i, N, i):
                sieve[j] = False


result = sum(prime_generator(N=2_000_000))


print(result)
