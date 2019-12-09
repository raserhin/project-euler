"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt, floor
from time import time


def divisors(x):
    divisors_list = []
    for i in [i for i in range(1, floor(sqrt(x)) + 1) if x % i == 0]:
        divisors_list.append(i)
        divisors_list.append(x // i)

    divisors_list.sort()
    return set(divisors_list)


def are_amicable(x, y):
    return sum(divisors(x)) == y and sum(divisors(y)) == x
# TODO: Optimize this code

N = 10000
array = []
start = time()
for i in range(1, N):
    if i % 50 == 0:
        print("\r", i, "Tiempo de momento {}".format(
            time() - start), array, end="")
    for j in range(1, i):
        if i != j and are_amicable(i, j):
            array.append(i)
            array.append(j)
