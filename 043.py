"""
Project Euler Problem 43
========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def permutations(digits):
    if len(digits) == 1:
        return [digits]
    else:
        results = []
        for i in range(len(digits)):
            subperms = permutations(digits[:i] + digits[i+1:])
            for s in subperms:
                results.append([digits[i]] + s)
        return results

def property(digits):
    return int(''.join(digits[1:4])) % 2 == 0 and int(''.join(digits[2:5])) % 3 == 0 and int(''.join(digits[3:6])) % 5 == 0 and int(''.join(digits[4:7])) % 7 == 0 and int(''.join(digits[5:8])) % 11 == 0 and int(''.join(digits[6:9])) % 13 == 0 and int(''.join(digits[7:10])) % 17 == 0

perms = permutations(['0','1','2','3','4','5','6','7','8','9'])

perms = [int(''.join(perm)) for perm in perms if property(perm)]

print sum(perms)


