"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
def prime_generator(N:int = 10):
    sieve = [False, False] + [True] * N  # Added 0 and 1

    for i in range(2, N+1):
        if sieve[i]:
            for j in range(i*i, N, i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime and is_circular_prime(i, sieve)}

def is_circular_prime(prime:int, sieve: list):
    str_prime = str(prime)
    for i in range(len(str_prime)):
        number = int(str_prime[i:len(str_prime)] + str_prime[0:i])
        if number %2 == 0 and prime != number:
            return False
        if not sieve[number]:
            return False
    return True



lookup_prime = prime_generator(1_000_000)

print(len(lookup_prime))
# for prime in lookup_prime:
#     print(prime)






