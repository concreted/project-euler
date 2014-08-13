"""
Project Euler Problem #31
==========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""

def change(available, total):
    if total == 0:
        return 1
    
    # Short circuit recursion if only one available coin 
    if len(available) == 1:
        if total % available[0] == 0:
            return 1

    if total <= 0 or available == []:
        return 0

    available_minus_largest = list(available)
    largest_available = available_minus_largest.pop()
    return change(available_minus_largest, total) + change(available, total - largest_available)

a = [1, 2, 5, 10, 20, 50, 100, 200]

total = 200

print change(a, total)
