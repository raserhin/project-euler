"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math import floor, sqrt, pow


def numDigits(number):
    return len(str(number))


def is_palindrome(pal):
    return str(pal) == str(pal)[::-1]


def twoMultiply(number, n):
    for i in range(floor(10**(n-1)), floor(sqrt(number))):
        if (number % i) == 0 and numDigits(floor(number / i)) == n:
            return True
    return False


n = 3  # Number of digits


result = max([i for i in range(int(pow(10, 2*(n-1))), int(pow(10, 2*n))) if is_palindrome(i) and twoMultiply(i, n)])
print(result)
