"""
Project Euler Problem #9
=========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

triplesum = 1000
c = 3
b = 2
a = 1

done = False

while a < triplesum:
    #print a,b,c
    if a*a + b*b == c*c and a + b + c == triplesum:
        print a*b*c
        quit()
    else:
        c += 1
        if a+b+c > triplesum:
            b += 1
            c = b + 1
            if a+b+c > triplesum:
                a += 1
                b = a+1
                c = b+1
    #inp = raw_input()

print "failed!"
print a*b*c
