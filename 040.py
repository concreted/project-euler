"""
Project Euler Problem #40
==========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12^th digit of the fractional part is 1.

If d[n] represents the n^th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

d = '.'
i = 1
limit = 1000000

while len(d) < limit+1:
    d += str(i)
    i += 1

print int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])
    
