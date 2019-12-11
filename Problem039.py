"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from time import time 
from math import sqrt, floor





N = 1000

lookup_table = [0]*(N+1)
for a in range(1, N):
    for b in range(a, N):
        c = sqrt(a*a+b*b)
        if c == floor(c):
            c = floor(c)
            p= a+b+c
            if p < N:
                lookup_table[p] += 1

print(lookup_table.index(max(lookup_table)))



