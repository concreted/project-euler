"""
Project Euler Problem #23
==========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

def factors(x):
    # Slow:
    return [i for i in range(1, x) if x%i == 0]

def abundant(x):
    return sum(factors(x)) > x

def abundantsLessThan(x):
    return [n for n in range(x) if abundant(n)]


# Positive integers which cannot be written as the sum of 
# two abundant numbers under a certain limit 

def P(limit):
    a = set(abundantsLessThan(limit + 1))
    result = []
    for i in range(limit):
        add = True
        for n in a:
            if (i - n) in a:
                add = False
        if add:
            result.append(i)

    return result

print sum(P(28123))
