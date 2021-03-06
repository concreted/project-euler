"""
Project Euler Problem 45
========================

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle     T[n]=n(n+1)/2   1, 3, 6, 10, 15, ...
Pentagonal   P[n]=n(3n-1)/2  1, 5, 12, 22, 35, ...
Hexagonal    H[n]=n(2n-1)    1, 6, 15, 28, 45, ...

It can be verified that T[285] = P[165] = H[143] = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
import math

def T(n):
    return n*(n+1) / 2

def isT(n):
    index = (math.sqrt(8*n + 1) - 1) / 2
    return int(index) == index


def P(n):
    return n*(3*n-1) / 2

def isP(n):
    index = (math.sqrt(1+24*n) + 1.0)/6.0
    return index == int(index)


def H(n):
    return n*(2*n-1)

def isH(n):
    index = (math.sqrt(1+8*n) + 1) / 4.0
    return index == int(index)

i = 40756
while True:
    if isT(i) and isP(i) and isH(i):
        print i
        break
    i += 1

