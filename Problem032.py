"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
from math import log10
from time import time

digits = [int(i) for i in "123456789"]


def is_sub_pandigital(x):
    return len(set(str(x)) ) == len(list(str(x)))

def is_pandigital(*args):
    flattern_string = "".join(str(arg) for arg in args)
    return len(set(flattern_string)) == len(flattern_string) == 9



start_time = time()
result = set()
for a in [_ for _ in range(100) if "0" not in str(_) and is_sub_pandigital(_)]:
    for b in [_ for _ in range(a, 10000) if "0" not in str(_) and  is_sub_pandigital(_)]:
        if "0" not in str(a*b) and is_pandigital( a, b, a*b):
            result.add(a*b)
final_time = time()

print(sum(result))