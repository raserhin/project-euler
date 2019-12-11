"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from math import sqrt, floor

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_seq(seq):
    result = 1
    for i in seq:
        result = lcm(result, i)
    return result


solution = lcm_seq(range(1,21))
print(solution)
