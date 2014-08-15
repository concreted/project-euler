"""
Project Euler Problem #37
==========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1
    
def truncated(n):
    digits = int(math.log(n, 10)) + 1
    return [n / (10**i) for i in range(digits)] + [n % (10**(i+1)) for i in range(digits)]


truncatable_primes = []
for i in range(11, 1000000):
    if prime(i) and all([prime(n) for n in truncated(i)]):
        truncatable_primes.append(n)

print sum(truncatable_primes)
