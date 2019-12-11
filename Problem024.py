"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from time import time
from math import factorial


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Nth = 1_000_000 - 1

result = []
while len(digits) > 0:
    new_digit = Nth // factorial(len(digits)-1)
    Nth %= factorial(len(digits) - 1)
    result.append(digits.pop(new_digit))

print("".join(str(i) for i in result))
