"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000
"""
import time

pair_of_numbers = [3, 5]
N = 1000  # This is the number that we have to find its divisibles


def sum_of_numbers(i):
    """
    Sum of all integers from 1 to N:
    
    Equivalent to ``sum(num for num in range(i+1))``
    """
    return int(i*(i+1)/2)

start_time = time.time()
result = sum_of_numbers((N-1) // 3) * 3 + 5 * \
    sum_of_numbers((N-1) // 5) - 15 * sum_of_numbers((N-1)//15)
final_time = time.time()
print(result)
