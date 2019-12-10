"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from time import time


def is_palindrom(i):
    return str(i) == str(i)[::-1]


def is_both_palindrom(i):
    return is_palindrom(i) and is_palindrom(bin(i)[2:])


N = int(1e6)

start = time()
result = [i for i in range(1, N + 1) if is_both_palindrom(i)]

print("The result {} has been found in {:.6f}s".format(
    sum(result), time() - start))
