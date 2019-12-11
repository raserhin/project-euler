"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from sympy import primefactors
from time import time 


n = 600851475143
factors = primefactors(n)
print(factors[-1])