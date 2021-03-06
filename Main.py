from Matrix import Matrix
from Inverse_Gauss import invert, gauss, determinant
from OnStart import OnStart
from copy import deepcopy
import math


# Evaluate points for the second discriminant function
def g2X(pointX, pointY):
    # mean points for M2
    x = -0.3983508496636363
    y = 1.650296255027272
    determinant = 1.0400422702555443
    invertedMatrix = [[1.6944441732616555, -0.08631020085280346],
                      [-0.08631020085280344, 0.5718387468650289]]

    meanMat = Matrix([[pointX - x], [pointY - y]])
    b = Matrix(meanMat.get_data())
    b.transpose()
    # multiply transposed by inverted covarince matrix
    first = b.multiply(Matrix(invertedMatrix))
    # multiply by regular matrix
    second = first.multiply(meanMat)
    second.scalar(-(1 / 2))
    final = second.get_data()[0][0] - 1 / 2 * math.log(determinant) + math.log(.5)
    return(final)


# Evaluate points for the first discriminant function
def g1X(pointX, pointY):
    # mean points for M2
    x = 2.131926754809091
    y = -1.980792810254546
    determinant = 2.1778184668732696
    invertedMatrix = [[1.8634294983642803, -0.08692972381503554],
                      [-0.08692972381503551, 0.25046929419146485]]

    meanMat = Matrix([[pointX - x], [pointY - y]])
    b = Matrix(meanMat.get_data())
    b.transpose()
    # multiply transposed by inverted covarince matrix
    first = b.multiply(Matrix(invertedMatrix))
    # multiply by regular matrix
    second = first.multiply(meanMat)
    second.scalar((-1 / 2))
    final = second.get_data()[0][0] - (.5 * math.log(determinant)) + math.log(.5)
    return(final)


def main():
    test = OnStart()

    print('Mean:')
    test.get_mean().print_data()
    x = test.get_mean().get_data()[0][0]
    y = test.get_mean().get_data()[0][1]

    print('\nCovariance:')
    test.get_covariance().print_data()

    print('\nDeterminant')
    print(test.get_covariance_determinant())

    print('\nInversion:')
    print(test.get_inverse())

    print('\nDiscriminant function results for m1 and m2:')

    # Evaluate the discriminant function at m1
    print()
    print("g1(m1)=", g1X(2.131926754809091, -1.980792810254546))
    print("g1(m2)=", g2X(2.131926754809091, -1.980792810254546))
    print("m1 therefore belongs in class 1.")
    # Evaluate the discriminant functon at m2
    print("g1(m2)=", g1X(-0.3983508496636363, 1.650296255027272))
    print("g2(m2)=", g2X(-0.3983508496636363, 1.65029625502727))
    print("m2 therefore belongs in class 2.")

    print('\nRunning  the data points through the discriminant functions:')
    # shift through the matricies and see which ones are mis-classified
    count = 0
    for n in test.matrices:
        if g1X(n.get_data()[0][0], n.get_data()[0][1]) > g2X(n.get_data()[0][0], n.get_data()[0][1]):
            continue
        else:
            print("Data Points", n.get_data()[0][0], n.get_data()[0][1], " are not in class 1")
            print("G1X:", g1X(n.get_data()[0][0], n.get_data()[0][1]))
            print("G2X:", g2X(n.get_data()[0][0], n.get_data()[0][1]))
            count += 1
    print("There are " + str(count) + " missclassified datapoints")

    # find datapoints such that | g1(x) - g2(x)| ≈ 0.0.
    print('\nEstimate and plot the boundary countour generated by the classifier')
    for n in test.matrices:
        if abs((g1X(n.get_data()[0][0], n.get_data()[0][1])) - (g2X(n.get_data()[0][0], n.get_data()[0][1]))) < .3:
            print("Data Points", n.get_data()[0][0], n.get_data()
                  [0][1], " to plot boundary marker point")

    print('\nGauss')
    system = [[3, 1, -1, 4, 1, 1, -1, -1, 2],
              [1, 2,  2, 0, -1, -2, 2, 2, -3],
              [0, -2, 5, 4, -1, 0, 3, 1, 4],
              [1, 1, -7, 3, 2, 2, -9, 0, -1],
              [1, 1, 2, 3, -2, 2, 2, 9, 1],
              [0, -3, -2, 2, 0, 2, 4, -5, -2],
              [-2, 1, -1, 1, 1, -5, 0, -2, 3],
              [1, 0, 1, 1, 0, 2, 1, 1, -4]]
    solved_system = [gauss(system)]
    print(solved_system)

    print('\nThe determinant of the coefficient matrix is ')
    coefficient_matrix = [[3, 1, -1, 4, 1, 1, -1, -1],
                          [1, 2,  2, 0, -1, -2, 2, 2],
                          [0, -2, 5, 4, -1, 0, 3, 1],
                          [1, 1, -7, 3, 2, 2, -9, 0],
                          [1, 1, 2, 3, -2, 2, 2, 9],
                          [0, -3, -2, 2, 0, 2, 4, -5],
                          [-2, 1, -1, 1, 1, -5, 0, -2],
                          [1, 0, 1, 1, 0, 2, 1, 1]]
    copy_coefficient_matrix = deepcopy(coefficient_matrix)
    print(determinant(copy_coefficient_matrix))

    print('\n The inverse of the coefficient matrix is ')
    inverted_coefficient_matrix = Matrix(invert(coefficient_matrix))
    inverted_coefficient_matrix.print_data()

    print('\n The determinant of A^-1')
    copy_inverted_coefficient = deepcopy(inverted_coefficient_matrix.get_data())
    print(determinant(copy_inverted_coefficient))

    print('\n the product of the determinants A and A^-1')
    product_of_determinant = -19511.999999999953 * -5.1250512505125055e-05
    print(product_of_determinant)

    print('\nIf A-1 exists, check your system solution results by performing the appropriate matrix multiplication and reporting the results.')

    b = Matrix([[2, -3, 4, -1, 1, -2, 3, -4]])
    b.transpose()
    # b.print_data()
    x = inverted_coefficient_matrix.multiply(b)
    print(x.get_data())

    print('\n Find the condition number for the coefficient matrix for the system')
    # Cond[A]= the norm[A] * norm[A-Inverse]
    row_total = 0
    list_norms_coefficient = []
    for x in coefficient_matrix:
        for y in x:
            row_total = row_total + abs(y)
        list_norms_coefficient.append(row_total)
        row_total = 0
    norm_ifinity_of_coefficient = (max(list_norms_coefficient))

    row_total_inverse = 0
    list_norms_inverse = []
    # same operation but for inverse
    for x in inverted_coefficient_matrix.get_data():
        for y in x:
            row_total_inverse += abs(y)
        list_norms_inverse.append(row_total_inverse)
        row_total_inverse = 0
    norm_inverse = (max(list_norms_inverse))
    condition_number = norm_inverse * norm_ifinity_of_coefficient

    print(condition_number)


main()
