"""
Project Euler Problem #41
==========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def permutations(digits):
    if len(digits) == 1:
        return [digits]
    else:
        results = []
        for i in range(len(digits)):
            subperms = permutations(digits[:i] + digits[i+1:])
            for s in subperms:
                results.append([digits[i]] + s)
        return results

perms = permutations([1,2,3,4,5,6,7])
perms.reverse()

for perm in perms:
    p = int(''.join([str(n) for n in perm]))
    if prime(p):
        print p 
        break
