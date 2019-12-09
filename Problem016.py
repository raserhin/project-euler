"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""
from time import time 
number = 2**1000

start_time = time()

result = sum(int(i) for i in str(number))

final_time = time()
print(f"The result {result} has been found in {final_time-start_time:.6f}s")

