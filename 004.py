"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(x):
    num_string = str(x)
    if num_string == num_string[::-1]:
        return True
    return False

three_digit_nums = range(999, 99, -1)

best = 0

for i in range(len(three_digit_nums)):
    for j in range(i, len(three_digit_nums)):
        candidate = three_digit_nums[i] * three_digit_nums[j]
        if isPalindrome(candidate):
            #print three_digit_nums[i], "*",  three_digit_nums[j], "=", candidate
            if candidate > best:
                best = candidate

print best
