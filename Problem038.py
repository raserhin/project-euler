"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
from time import time 
from math import log10, floor

def is_pandigital(x, n):
    digits = "".join(str(x*i) for i in range(1, n+1))
    return len(digits) == len(set(digits)) == 9 and "0" not in digits



start_time = time()

a= [(i, 9 // (floor(log10(i)) + 1))  for i in range(1,10_000) if is_pandigital(i, 9 // (floor(log10(i)) + 1))]
result = [  "".join(str(x*i) for i in range(1, n+1)) for x, n in a]

final_time = time()
print(max(result))