"""
Project Euler Problem #3
=========================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def isPrime(x):
    for i in range(2, x/2 + 1):
        if x % i == 0:
            return False
    return True

num = 600851475143
best = 3
i = 3

while i < num/2 + 1:
    if num % i == 0:
        print i
        '''
        if isPrime(i):
            best = i
            print best
        '''
    i += 1
print best
        

