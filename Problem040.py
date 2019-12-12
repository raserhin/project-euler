"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                    123456789012345

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""
from math import log10, floor


def digit_generator(N=1_000_000):
    """ Generator of the N first digits of the concatenation """
    i = 0
    number = 1
    while N > i:
        for _i in str(number):
            yield _i
            i += 1
        number += 1




def get_digit(n):
    """ Get the digit in nth decimal place"""
    """
    9           -   9
    10-99       -   2*90 
    100-999     -   3*900
    """
    i = 0
    start = 0
    done = False
    while not done:
        step = (i+1)*9*(10**i)
        if start + step > n:
            done = True
        else:
            start += step
            i += 1

    num_digits = i + 1

    offset = n - start
    number = offset // num_digits + \
        (10**(num_digits-1) if (num_digits - 1) else 0)
    _i = (offset - 1) % num_digits
    print(number)
    return int(str(number)[_i])




result = 1

for i in range(0, 7):
    result *= get_digit(10**i)
print(result)
