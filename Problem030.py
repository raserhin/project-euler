"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
from time import time


def is_sum_digits(x, power=4):
    return x == sum([int(i)**power for i in str(x)])


start_time = time()
_result = [i for i in range(2, 6*9**5) if is_sum_digits(i, power=5)]
result = sum(_result)
final_time = time()


print(f"The result {result} has been found in {final_time - start_time:.6f}")
