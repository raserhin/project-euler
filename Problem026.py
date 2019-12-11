"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from time import time 


def recurring_cycle_length(divisor: int, dividend: int = 1):
    lookup_dividend = []
    remaining = 1
    while dividend and remaining:
        while dividend < divisor:
            dividend *= 10
        remaining, dividend = dividend // divisor, dividend % divisor
        if (dividend, remaining) in lookup_dividend:
            index = lookup_dividend.index((dividend, remaining))
            return len(lookup_dividend[index:])

        lookup_dividend.append((dividend, remaining))
    return 0


N = 1000
result = max([(recurring_cycle_length(i), i) for i in range(1, N)])
print(result[1])