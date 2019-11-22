"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt, ceil
from time import time


def prime_generator(N=10):
    yield 2
    for i in range(3, N, 2):
        is_prime = True
        for divisor in range(3, ceil(sqrt(i)) + 1, 2):
            if i % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield i


start_time = time()
result = sum(prime_generator(N=2_000_000))
elapsed = time() - start_time

print("The result [{}] has been found in {:.6f}s".format(result, elapsed))
