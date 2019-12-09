"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from math import log10, floor
from time import time

def fibonacci():
    """
        Infinite Generator of fibonacci sequence
    """
    a, b = 1, 2
    yield 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


num_digits = 1_000
start_time = time()
for i, term in enumerate(fibonacci()):
    if floor(log10(term)) +1  == num_digits :
        result = i + 1
        break
    
final_time = time()

print(f"The result {result} has been found in {final_time - start_time:.6f}")
