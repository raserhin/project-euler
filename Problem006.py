"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

N = 100
natural_sum = sum((i*i for i in range(1, N+1)))
sum_squared = sum((i for i in range(1, N + 1)))**2


print("Sum of squares ={} ".format(natural_sum))
print("Squared of the sum ={}".format(sum_squared))
print("The difference is = {}".format(sum_squared - natural_sum))
