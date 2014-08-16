"""
Project Euler Problem #39
==========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

limit = 1000

best = 0
solutions = []

def components(n):
    results = []
    a = 1
    b = 2
    c = n-3
    
    results.append((a,b,c))
    
    while(True):
        if (b+1 < c-1):
            b += 1
            c -= 1
        else:
            a += 1
            b = a + 1
            c = n - (a+b)
            if (b >= c):
                break

        results.append((a,b,c))

    return results

for p in range(limit):
    current_solutions = []
    for component in components(p):        
        a,b,c = component
        if a+b+c == p and a**2 + b**2 == c**2:
            current_solutions.append((a,b,c))
    if len(current_solutions) > len(solutions):
        solutions = current_solutions
        best = p

print best
