"""
Project Euler Problem #14
==========================

The following iterative sequence is defined for the set of positive
integers:

n n/2 (n is even)
n 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                         13 40 20 10 5 16 8 4 2 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatzSequence(n):
    if n > 0:
        seq = [n]
    else:
        return []

    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        seq.append(n)
    
    return seq    

def longestChain(maxnum):
    best_len = 0
    best_n = 0
    for n in range(1, maxnum):
        current = len(collatzSequence(n))
        if current > best_len:
            best_len = current
            best_n = n
    return best_n, best_len

print longestChain(1000)
