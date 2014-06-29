"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import math

def factors(x):
    return set([i for i in range(2, x/2 + 1) if x%i == 0])

maximum = 20
candidate = maximum

check_vals = set(range(2, maximum+1))

for i in range(maximum, 2, -1):
    fac = factors(i)
    check_vals.difference_update(fac)

#print check_vals

def evenlyDivisible(x, maximum):
    x_factors = factors(x)
    
    nul = all_factors.difference(x_factors)
    
    if nul == set():
        return True
    return False

def evenlyDivisibleBasic(x, maximum):
    for i in range(maximum, 1, -1):
        if x % i != 0:
            return False        
    return True

def evenlyDivisibleFast(x, maximum):
    for i in check_vals:
        if x % i != 0:
            return False
    return True

while True:
    if evenlyDivisibleFast(candidate, maximum):
        print candidate
        quit()
    candidate += maximum

