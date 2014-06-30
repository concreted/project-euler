"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import math

# Source: http://stackoverflow.com/questions/16996217/prime-factorization-list
def primeFactors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def countOccur(numbers):
    counts = {}
    for i in numbers:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

maximum = 20

all_factors = set(range(2, maximum+1))

primes = list(all_factors)
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if primes[j] != 0 and primes[i] != 0 and primes[j] % primes[i] == 0:
            primes[j] = 0
    
primes = countOccur(set([i for i in primes if i != 0]))

all_factors.difference_update(primes)
all_factors = list(all_factors)

#print all_factors
#print primes

for i in all_factors:
    vals = countOccur(primeFactors(i))
    #print vals
    for n in vals:
        if vals[n] > primes[n]:
            primes[n] = vals[n]

#print primes

print reduce(lambda acc, n: acc * n ** primes[n], primes, 1)
