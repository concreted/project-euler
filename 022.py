"""
Project Euler Problem #22
==========================

Using names.txt [http://projecteuler.net/project/names.txt], a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

def alphaVal(name):
    total = 0

    # Assumes name is all caps
    for i in range(len(name)):
        total += ord(name[i]) - 64

    return total

names = open('names.txt', 'r')

lines = [name[1:len(name)-1] for name in names.readlines()[0].split(',')]

names.close()

lines.sort()

#print alphaVal(lines[937]) * 938 == 49714

total = 0

for i in range(len(lines)):
    total += alphaVal(lines[i]) * (i+1)

print total
