# Matrix 1: [[3,4,5], [1,6,7], [7,4,6]]
# Matrix 2: [[4,3,6], [5,3,5], [4,7,2]]

def matrix_multiplication(A, B):
    n = len(A)
    C = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            C[i,j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
