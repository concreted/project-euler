"""
Project Euler Problem #32
==========================

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

'''
Get all permutations of string 123456789.

Check for solutions, fixing combined length of multiplicand and multiplier to
at least 5 digits. 

If lengths of multiplicand/multiplier total 5 digits, resulting products are
in range 2345 (2345*1) to 78885 (8765*9). That covers all four-digit products.

If lengths of multiplicand/multiplier are less/greater than 5 digits, product 
will be too short/long to cover all digits (123456789).
'''

def perms(s):
    if len(s) == 1:
        return s
    result = []
    for r in s:
        for perm in perms(s.replace(r, '')):
            result.append(r + perm)
    return result

permutations = perms('123456789')
prods = set()
total = 0
for l in range(1, 5):
    for p in permutations:
        ldigits = int(p[:l])
        rdigits = int(p[l:5])
        prod = int(p[5:])
        
        if ldigits * rdigits == prod and prod not in prods:
            #print ldigits, "*", rdigits, "=", prod
            prods.add(prod)
            total += prod
print total
