"""
Project Euler Problem #15
==========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

def findPaths(grid_size):
    def walkGrid(x,y):
        if x == grid_size and y == grid_size:
            return 1
        elif x == grid_size:
            return walkGrid(x, y+1)
        elif y == grid_size:
            return walkGrid(x+1, y)
        else:
            return walkGrid(x+1, y) + walkGrid(x, y+1)
    return walkGrid(0,0)

print findPaths(1) == 2
print findPaths(2) == 6
print findPaths(3) == 20
print findPaths(4) == 70
print findPaths(5) == 252
