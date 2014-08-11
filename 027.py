"""
Project Euler Problem #27
==========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                                e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

def consecutivePrimes(a, b):
    n = 0
    current = n**2 + a*n + b
    while (prime(current)):
        n += 1
        current = n**2 + a*n + b
    return n

#print consecutivePrimes(1, 41) == 40
#print consecutivePrimes(-79, 1601) == 80

best_a = 0
best_b = 0
most_consecutive = 0
lower = -999
higher = 1000

for a in range(lower, higher):
    for b in range(lower, higher):
        current = consecutivePrimes(a, b)
        if current > most_consecutive:
            most_consecutive = current
            best_a = a
            best_b = b

print best_a * best_b
        
