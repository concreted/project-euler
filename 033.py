"""
Project Euler Problem #33
==========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

def curiousFractions():
    result = []
    for num in range(10, 100):
        for den in range(num+1, 100):
            quotient = float(num)/den
            try:
                if ((float(num/10) / (den % 10)) == quotient and num % 10 == den/10) or ((float(num % 10)  / (den/10)) == quotient and num/10 == den%10):
                    result.append((num, den))
            except:
                continue
    return result

def gcd(fraction):
    num, den = fraction
    if num == den:
        return num
    if num > den:
        return gcd((num-den, den))
    else:
        return gcd((num, den-num))

def simplify(fraction):
    divisor = gcd(fraction)
    num, den = fraction
    return (num/divisor, den/divisor)

cf = curiousFractions()
#print cf

cf_num = reduce(lambda acc, n: acc * n[0], cf, 1)
cf_den = reduce(lambda acc, n: acc * n[1], cf, 1)

#print cf_num, cf_den
print simplify((cf_num, cf_den))[1]

