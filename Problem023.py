"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import sqrt, floor
from time import time 

def get_divisors(x):
    divisors = {1}
    for i in [i for i in range(2, floor(sqrt(x)) + 1) if x % i == 0]:
        divisors.update([i, x//i])
    return divisors

def is_abundant(x):
    return x < sum(get_divisors(x))

def is_sum_abundant(x, lookup_abundant):
    tmp = filter(lambda item: item < x, lookup_abundant)
    for i in tmp:
        if x-i in lookup_abundant:
            return True
    return False


N = 28123

start_time = time()
lookup_abundant = {i for i in range(1, N+1) if is_abundant(i)}
# print(get_divisors(12))
# print(is_sum_abundant(24, lookup_abundant))
is_not_sum = [i for i in range(1, N+1) if not is_sum_abundant(i, lookup_abundant)]
result = sum(is_not_sum)
final_time = time()

print(f"The result {result} has been found in {final_time - start_time:.6f}")