"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


def prime_generator(N=10):
    sieve = [False, False] + [True] * N  # Added 0 and 1

    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i*i, len(sieve), i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def find_max(prime_list, N=1_000_000):
    max_n = 0
    current = 0
    for prime in prime_list:
        current += prime 
        if current > N:
            return max_n
        max_n += 1
    return 0

N = 1_000_000

prime_list = prime_generator(1_000_000)
lookup_prime = set(prime_list)

max_value = 0 
n = find_max(prime_list, N)
found = False
while not found:
    i=0
    while len(prime_list) + n > i:
        if i > 0 and n % 2 == 0:
            break 
        current = sum(prime_list[i:i+n])
        if current > N:
            break
        elif current in prime_list:
            max_value = max(current, max_value)
            found = True
            break
        i+=1
    n-=1
print(max_value)
