"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a*a + b*b = c*c
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from time import time


def get_triplet(N=1000):

    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a*a+b*b == c*c:
                return a, b, c


start_time = time()
a, b, c = get_triplet()
elapsed = time() - start_time

print(f"The found triplet is {a}, {b}, {c}.")
print(f"Result: {a*b*c} found in {elapsed:.6f}s ")
