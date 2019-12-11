"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""
from time import time

def prime_generator(N=10):
    sieve = [False, False] + [True] * N # Added 0 and 1 
    
    for i in range(2, N+1):
        if sieve[i]:
            for j in range(i*i, N, i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime}



lookup_prime = prime_generator(1_000_000)
N = 1000
max_n = 0

for b in (i for i in range(-N+1, N, 2) if abs(i) in lookup_prime):
    for a in (i for i in range(-N+1, N, 2)):
        n=0
        while n*n+a*n+b in lookup_prime:
            n+=1
        if n > max_n:
            max_n = n
            result= a*b

print(result)
