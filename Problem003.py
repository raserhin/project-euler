"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from sympy import primefactors
from time import time 


n = 600851475143
start_time = time()
factors = primefactors(n)
final_time = time()
print(f"The result {factors[-1]} has been found in {final_time-start_time:.6f}s")