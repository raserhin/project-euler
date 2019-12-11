"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from time import time
from math import factorial

def is_curious(x):
    return sum(factorial(int(i)) for i in str(x)) == x


start_time = time()
result = [i for i in range(3, 50_000) if is_curious(i) ]
final_time = time()

print(sum(result))
