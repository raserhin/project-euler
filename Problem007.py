"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import floor, sqrt


def isPrime(x):
    if x in [2, 3, 5]:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(3, floor(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


a = 0
prime_number = 10001
num = 2
while(True):
    if isPrime(num):
        a += 1
        print(a, num)
        if a == prime_number:
            break
    num += 1

print(f"The prime number {a} is {num}")
