"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""
import math

def wordToValue(word):
    word = [ord(c) - 64 for c in list(word.upper())]
    return sum(word)

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    return (x1, x2)

def isTriangleNumber(n):
    index, other = quadratic(1,1,-2*n)
    return int(index) == index

f = open('resources/words.txt')
words = f.readlines()[0].replace('"', '').split(',')
f.close()
        
count = 0
for word in words:
    if isTriangleNumber(wordToValue(word)):
        count += 1
print count
