# Helper functions for the inverse and determinant calculations


# swap the row i with row j in the list of lists
def swap_row(matrix, i, j):
    matrix[j], matrix[i] = matrix[i], matrix[j]
    return(matrix)


# make an identity matrix with the specified dimensions
def make_identity_matrix(x, y):
    identity = []
    for i in range(0, x):
        row = []
        for j in range(0, y):
            elem = 0
            if i == j:
                elem = 1
            row.append(elem)
        identity.append(row)
    return(identity)


# check the matrix and see if only zeros are below row i and j
def check_for_zeros(matrix, i, j):
    not_zeros = []
    # index of first non-zero value
    first_not_zero = -1
    for m in range(i, len(matrix)):
        not_zero = matrix[m][j] != 0
        not_zeros.append(not_zero)
        if first_not_zero == -1 and not_zero:
            first_not_zero = m
    # zero sum is count of non-zero entries
    zero_sum = sum(not_zeros)
    return(zero_sum, first_not_zero)
