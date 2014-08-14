"""
Project Euler Problem #35
==========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def rotations(n):
    num_digits = int(math.log(n, 10)) + 1
    result = [n]
    for i in range(1, num_digits):
        last_digit = result[i-1] % 10
        r = result[i-1] / 10 + (last_digit * 10**(num_digits-1))
        result.append(r)
    return result

def circularPrimes(limit):
    result = []
    for i in range(2, limit + 1):
        if prime(i) and all([prime(n) for n in rotations(i)]):
            result.append(i)
    return result

limit = 1000000

print len(circularPrimes(limit))
