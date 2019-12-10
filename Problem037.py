"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from time import time
from math import log10


def prime_generator(N=10):
    sieve = [False, False] + [True] * N  # Added 0 and 1

    for i in range(2, N+1):
        if sieve[i]:
            for j in range(i*i, N, i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime}


def is_truncable(x):
    right = [x//10**i for i in range(1, int(log10(x) + 1))]
    left = [x % 10**(i+1) for i in range(int(log10(x)))]
    return all([i in lookup_prime for i in right+left])


lookup_prime = prime_generator(1_000_000)

start_time = time()


result = [i for i in lookup_prime if log10(i) > 1 and str(
    i)[-1] in ("37") and str(i)[0] in ("2357") and is_truncable(i)]
final_time = time()

print(f"The result {sum(result)} has been found in {final_time - start_time:.6f}s")
