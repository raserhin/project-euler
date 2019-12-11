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
            i+=1
        number+=1

def get_digit(n):
    """ Get the digit in nth decimal place"""
    """
    9           -   9
    10-99       -   2*90 
    100-999     -   3*900
    """
    i = 0
    start = 0
    while start < n: 
        start += (i+1)*9*(10**i)
        i += 1
    

    num_digits = i + 1
    print(start, num_digits)

    offset =  n -  start
    number = offset // num_digits + 10**(num_digits-1) - 1
    _i = (offset + 1) % num_digits
    print(n, start, offset, number, _i)
    print(str(number)[_i])



get_digit(11)
get_digit(12)
get_digit(13)
get_digit(14)
get_digit(15)
get_digit(16)
get_digit(100)


# for i in range(0, 7):
#     get_digit(10**i)


# result = 1
# for i, value in enumerate(digit_generator(N=1_000_000)):
#     a= log10(i+1)
#     if a == floor(a):
#         result *= int(value)
# print(result)

