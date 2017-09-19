class Matrix:
    def __init__(self, data):
        self.data = data
        self.columns = len(data[0])
        self.rows = len(data)
        self.size = [self.rows, self.columns]

    # setters for the matrix class
    def set_rows(self):
        self.rows = len(self.data)
        self.set_size()

    def set_cols(self):
        self.columns = len(self.data[0])
        self.set_size()

    def set_size(self):
        self.size = [self.rows, self.columns]

    # getters for the matrix classs
    def get_data(self):
        return self.data

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.columns

    def get_size(self):
        return self.size

    # Operations for the matrix class

    # Returns the identity matrix for any matrix
    def identity(self):
        identity = [[0] * x + [1] + [0] * (self.columns - x - 1) for x in range(self.rows)]
        return(Matrix(identity))

    # Returns the null matrix for a square matrix
    def zero(self):
        result = []
        for x in range(self.rows):
            result.append([0] * self.columns)
        return Matrix(result)

    # Transposes a Matrix
    def transpose(self):
        self.data = [list(x) for x in zip(*self.data)]
        self.set_cols()
        self.set_rows()

    # Scales each item of a matrix by a number
    def scalar(self, number):
        for x in self.data:
            for y in range(self.columns):
                x[y] = x[y] * number

    # return the result of adding two matrices
    def add(self, other):
        if self.size == other.size:
            result = []
            for x in range(self.rows):
                row = []
                for y in range(self.columns):
                    row.append(self.data[x][y] + other.data[x][y])
                result.append(row)
            return Matrix(result)
        else:
            return self.zero()

    # Returns the result of subtracting of two matrices
    def subtract(self, other):
        if self.size == other.size:
            res = []
            for x in range(self.rows):
                row = []
                for y in range(self.columns):
                    row.append(self.data[x][y] - other.data[x][y])
                res.append(row)
            return Matrix(res)
        else:
            return self.zero()

    # Returns the output of two matrices multiplied
    def multiply(self, other):
        if self.columns == other.rows:
            answer = []

            for x in range(self.rows):
                answer.append([0] * other.columns)

            for x in range(self.rows):
                for y in range(other.columns):
                    for z in range(other.rows):
                        answer[x][y] += self.data[x][z] * other.data[z][y]

            return Matrix(answer)
        else:
            return self.zero()

    # Prints the matrix in a easy to view format
    def print_data(self):
        for x in range(self.rows):
            print(self.data[x])
