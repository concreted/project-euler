"""
Project Euler Problem #28
==========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

ru_vals = [1]
rd_vals = [1]
lu_vals = [1]
ld_vals = [1]

def ru_cache(n):
    size = n + n + 1
    offset = (size-1) * 4
    current = ru_vals[n-1] + offset
    ru_vals.append(current)
    return current

def rd_cache(n):
    size = n + n + 1
    offset = ((size-3) * 2) + ((size-2) * 2)
    current = rd_vals[n-1] + offset
    rd_vals.append(current)
    return current

def lu_cache(n):
    size = n + n + 1
    offset = ((size-3)) + ((size-1)*3)
    current = lu_vals[n-1] + offset
    lu_vals.append(current)
    return current

def ld_cache(n):
    size = n + n + 1
    offset = size-3 + ((size-2)*3) + 1
    current = ld_vals[n-1] + offset
    ld_vals.append(current)
    return current

limit = 500

print sum([ru_cache(n) for n in range(1, limit+1)] + [rd_cache(n) for n in range(1, limit+1)] + [lu_cache(n) for n in range(1, limit+1)] + [ld_cache(n) for n in range(1, limit+1)]) + 1
