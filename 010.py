"""
Project Euler Problem #10
==========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

'''
#Solution:

print 142913828922
quit()
'''

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primeCount = 0
i = 2
limit = 2000000
primes = []

while i < limit:
    if isPrime(i):
        primeCount += 1
        primes.append(i)
    i += 1

#print primes
print sum(primes)

