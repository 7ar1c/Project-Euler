## Project Euler Q81 Solution
## Find the minimal path sum from the top left to the bottom right by moving right and down in matrix.txt
import numpy as np
matrix = np.loadtxt('0081_Matrix.txt', delimiter=',', dtype=int)

def minimal_path_sum(matrix):
    n = len(matrix)
    for i in range(1, n):
        matrix[i][0] += matrix[i-1][0]
        matrix[0][i] += matrix[0][i-1]
    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
    return matrix[n-1][n-1]

print(minimal_path_sum(matrix))