"""
Project Euler Problem #34
==========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

"""
Can naively bound solution by 9! * 7.

9!*7 == 2540160, which is 7 digits long. Potentially there could be 7-digit
numbers equal to sum of factorial of their digits.

9!*8 == 2903040, which is also 7 digits. This means there cannot be any 
8-digit numbers equal to the sum of factorial of their digits. 
"""

import math

total = 0
limit = (math.factorial(9) * 7) + 1
for n in range(3, limit):
    fact_sum = 0
    number = n
    while n > 0:
        digit = n % 10
        n = n / 10
        fact_sum += math.factorial(digit)
    if fact_sum == number:
        total += number

print total
