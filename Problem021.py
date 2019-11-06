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
