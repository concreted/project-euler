"""
Project Euler Problem #7
=========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6^th prime is 13.

What is the 10001^st prime number?
"""
import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primeCount = 0
i = 2
howMany = 10001

while primeCount < howMany:
    if isPrime(i):
        primeCount += 1
    i += 1

print i-1



