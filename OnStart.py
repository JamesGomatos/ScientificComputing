from Matrix import Matrix
from copy import deepcopy
from Inverse_Gauss import invert, determinant


class OnStart:
    def __init__(self):
        self.data = []
        self.matrices = []
        self.mean = Matrix([[0, 0]])
        self.covariance = Matrix([[0, 0], [0, 0]])
        self.determinant = 0
        self.inverse = []
        self.onStart()
        self.find_mean()
        self.find_covariance()
        self.find_covariance_determinant()
        self.find_inverse_covariance_matrix()

    # Read in the data.
    def onStart(self):
        temp = []
        filename = open('classOne.txt', 'r')
        for line in filename:
            row = line.strip()
            temp.append(row)
        for i in range(0, len(temp)):
            self.data.append(temp[i].split())
        for i in self.data:
            matrix = Matrix([[float(i[0]), float(i[1])]])
            self.matrices.append(matrix)

    # find the determinant of the covariance matrix
    def find_covariance_determinant(self):
        copy_matrix = deepcopy(self.covariance.get_data())
        self.determinant = determinant(copy_matrix)

    # find the inverse of the covariance matrix
    def find_inverse_covariance_matrix(self):
        self.inverse = invert(self.covariance.get_data())

    # Find the mean of the read-in data
    def find_mean(self):
        for x in self.matrices:
            self.mean = self.mean.add(x)
        self.mean.scalar(1 / len(self.matrices))

    # Find the covariance of the read-ion data
    def find_covariance(self):
        for x in self.matrices:
            val = x.subtract(self.mean)
            val_transposed = Matrix(val.get_data())
            val_transposed.transpose()
            result = val_transposed.multiply(val)
            self.covariance = self.covariance.add(result)

        self.covariance.scalar(1 / len(self.matrices))

    # getter methods

    def get_inverse(self):
        return self.inverse

    def get_covariance_determinant(self):
        return self.determinant

    def get_mean(self):
        return self.mean

    def get_covariance(self):
        return self.covariance
