"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from math import log, floor
from time import time


def collatz_sequence(n):
    if n in collatz_map:
        return collatz_map[n]
    elif bin(n).count("1") == 1:
        collatz_map[n] = floor(log(n, 2)) + 1
        return floor(log(n, 2)) + 1
    else:
        next_n = n//2 if n % 2 == 0 else 3*n+1 
        collatz_map[n] = collatz_sequence(next_n) + 1
        return collatz_map[n]


collatz_map = {}
MAX = 1_000_000


max_value = 0
result = 0
for i in range(MAX // 2, MAX ):
    current = collatz_sequence(i)
    if current > max_value:
        result = i
        max_value = current


print(result)
