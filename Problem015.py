"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

from math import factorial, floor
from time import time

n = 20
m = 2 * n - 1

start_time = time()
result = floor(2 * factorial(m) / factorial(m - n) / factorial(n))
final_time = time()
print(result)