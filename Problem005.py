"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from math import sqrt, floor


def isDivisible(number, divisors):
    boolean = True
    for divisor in divisors:
        if not number / divisor == 0:
            boolean = boolean and False
    return boolean


def isPrime(number):
    if(number % 2 == 0):
        return True
    for i in range(3, floor(sqrt(number)), 2):
        if number % i == 0:
            return True
    return False


def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

    return lcm


def lcm_list(divisors):
    _lcm = 1
    for i in divisors:
        _lcm = lcm(i, _lcm)
    return _lcm


min_divisor = 1
max_divisor = 20

divisors = [i for i in range(min_divisor, max_divisor + 1)]

print(lcm_list(divisors))
