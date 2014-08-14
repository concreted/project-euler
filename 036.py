"""
Project Euler Problem #36
==========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

limit = 1000000

total = 0

for n in range(limit):
    decimal = str(n)
    binary = str(bin(n))[2:]
    if decimal == decimal[::-1] and binary == binary[::-1]:
        total += n

print total
