"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from time import time 
from math import sqrt, floor





N = 1000

lookup_table = {}
for a in range(1, N):
    for b in range(a, N):
        c = sqrt(a*a+b*b)
        if c == floor(c):
            lookup_table[a+b+floor(c)] += 1

print(lookup_table)



