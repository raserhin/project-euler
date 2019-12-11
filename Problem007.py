"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import floor, sqrt


def prime_generator(N=10):
    sieve = [False, False] + [True] * N  # Added 0 and 1

    for i in range(2, N+1):
        if sieve[i]:
            yield i
            for j in range(i*i, N, i):
                sieve[j] = False
    




prime_index = 10001
for i, prime in enumerate(prime_generator(prime_index*100)):
    if i +1 == prime_index:
        print(prime)
        break

