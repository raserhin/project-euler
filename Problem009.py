"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a*a + b*b = c*c
For example, 3*3 + 4*4 = 9 + 16 = 25 = 5*5.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from time import time


def get_triplet(N=1000):

    for a in range(1, 999):
        for b in range(a, 999):
            c = 1000 - a - b
            if a*a+b*b == c*c:
                return a, b, c


start_time = time()
a, b, c = get_triplet()
elapsed = time() - start_time

print(a*b*c)
