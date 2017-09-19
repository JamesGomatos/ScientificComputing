from copy import deepcopy
from ListMatrixHelperFunctions import *


# return an inverse of a matrix using Gauss-Jordan elimination
def invert(input_matrix):
    # make a copy of matrix to avoid altering input matrix
    matrix = deepcopy(input_matrix)

    rows = len(matrix)
    columns = len(matrix[0])

    # Find the identity matrix and append it to the right
    identity = make_identity_matrix(rows, columns)
    for i in range(0, rows):
        matrix[i] += identity[i]
    i = 0
    for j in range(0, columns):
        # Check to see if there are any nonzero values
        zero_sum, first_not_zero = check_for_zeros(matrix, i, j)
        if zero_sum == 0:
            if j == columns:
                return matrix
        # swap the rows
        if first_not_zero != i:
            matrix = swap_row(matrix, i, first_not_zero)
        # Divide matrix[i] by matrix[i][j]
        matrix[i] = [m / matrix[i][j] for m in matrix[i]]
        # make all other rows values 0 below X[i][j]
        for q in range(0, rows):
            if q != i:
                row_scaled = [matrix[q][j] * m for m in matrix[i]]
                matrix[q] = [matrix[q][m] - row_scaled[m] for m in range(0, len(row_scaled))]
        # If either is true, we are done
        if i == rows or j == columns:
            break
        i += 1
    # get the right hand matrix
    for i in range(0, rows):
        matrix[i] = matrix[i][columns:len(matrix[i])]
    return(matrix)


# returns the determinant of the matrix
def determinant(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    det = 1.0
    for i in range(rows):
        row = i
        for j in range(i + 1, rows):
            if abs(matrix[j][i]) > abs(matrix[row][i]):
                # Swap rows and flip the det sign
                row = j
                swap_row(matrix, i, row)
                det *= -1
        for j in range(i + 1, rows):
            # divide by the diagonal of matrix
            temp = matrix[j][i] / matrix[i][i]
            for c in range(i, cols):
                # compute final diagonal values
                matrix[j][c] -= matrix[i][c] * temp
    for i in range(rows):
        # multiply determinant by the diagonal
        det *= matrix[i][i]
    return(det)


# Implement gauss-jordan elimination to solve a system
# input the system as a matrix that includes
# the coefficient matrix  concatenanted with the matrix of constants
def gauss(matrix):
    rows = len(matrix)

    for i in range(0, rows):
        # Find the maximum value for this column
        num = abs(matrix[i][i])
        row = i
        for j in range(i + 1, rows):
            if abs(matrix[j][i]) > num:
                num = abs(matrix[j][i])
                row = j
        # Switch the max row and current row
        for j in range(i, rows + 1):
            temp = matrix[row][j]
            matrix[row][j] = matrix[i][j]
            matrix[i][j] = temp
        # Make the rows below this one 0 in the current column
        for q in range(i + 1, rows):
            c = -matrix[q][i] / matrix[i][i]
            for j in range(i, rows + 1):
                if i == j:
                    matrix[q][j] = 0
                else:
                    matrix[q][j] += c * matrix[i][j]
    # Solve the equation for the matrix
    final = [0] * rows
    for i in range(rows - 1, -1, -1):
        final[i] = matrix[i][rows] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][rows] = matrix[j][rows] - matrix[j][i] * final[i]
    return(final)
