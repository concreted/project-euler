"""
Project Euler Problem #20
==========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

import math

print sum([int(i) for i in list(str(math.factorial(100)))])
