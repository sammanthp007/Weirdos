# You are given a matrix a. From any cell (i, j), you can move either in the
# right or downwards, i.e., either to cell (i, j + 1) or (i + 1, j). You are 
# initially at cell (0, 0) and want to reach at cell (m - 1, n - 1). Note that
# each cell has two values either 0 or 1. If the values at any cell is 1, then
# you can move through that cell, otherwise you cannot move.

# Complete the function numberOfPaths, that has one parameter, m * n matrix a.
# The function should return total number paths possible from cell (0, 0) to
# (m - 1, n - 1), as the answer could be large, return its value mod (10^9 + 7)

def numberOfPaths(matrix):
    return numOfPathsRecur(matrix, 0, 0)

def numOfPathsRecur(matrix, row, col):
    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return 0

    if row == len(matrix) - 1:
        if matrix[row][col] == 0:
            return -1
        return numOfPathsRecur(matrix, row, col + 1)

    if col == len(matrix[0]) - 1:
        if matrix[row][col] == 0:
            return -1
        return numOfPathsRecur(matrix, row + 1, col)

    return 1 + numOfPathsRecur(matrix, row + 1, col) + 1 + numOfPathsRecur(matrix, row, col + 1)

#matrix = [[1,1,1,1], [1,1,1,1], [1,1,1,1] ]
#matrix = [[1,1],[0,1]]
matrix = [[1,1,0], [1,1,1],[1,1,1],[0,0,1]]
print (numberOfPaths(matrix))
#r = 0
#c = 0
#m_r = 3, m_c = 2
#tot = 1 + () + 1 + ()
#tot = 1 + (1 + () + 1 + ()) + 1 + ()
"""
1 1 0
1 1 1
1 1 1
0 0 1

5"""
