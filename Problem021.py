"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt, floor
from time import time


def get_divisors(x):
    divisors = {1}
    for i in [i for i in range(2, floor(sqrt(x))) if x % i == 0]:
        divisors.update([i, x//i])
    return divisors


result = 0
N = 10_000
start_time = time()
for i in range(1, N + 1):
    target = sum(get_divisors(i))
    if i < target and i == sum(get_divisors(target)):
        result+= i+target
        print(i, target, result)

final_time = time()    

print(f"Found the result {result} in {final_time - start_time:.6f}s")
    
    
