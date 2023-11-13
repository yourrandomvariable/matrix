class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def display(self):
        for row in self.matrix:
            print(row)

    @property
    def rows(self):
        return len(self.matrix)

    @property
    def cols(self):
        return len(self.matrix[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [[self.matrix[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
            result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(other.rows)) for j in range(other.cols)] for i in range(self.rows)]
        else:
            raise ValueError("Unsupported type for multiplication.")
        return Matrix(result)

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            result = [[self.matrix[i][j] / scalar for j in range(self.cols)] for i in range(self.rows)]
        else:
            raise ValueError("Unsupported type for division.")
        return Matrix(result)

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("Exponent must be a non-negative integer.")
        result = self
        for _ in range(exponent - 1):
            result *= self
        return result

matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[2, 0], [1, 3]])

result_add = matrix1 + matrix2
result_subtract = matrix1 - matrix2
result_multiply = matrix1 * matrix2
result_scalar_division = matrix1 / 2
result_power = matrix1 ** 2

print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()

print("\nAddition:")
result_add.display()

print("\nSubtraction:")
result_subtract.display()

print("\nMultiplication:")
result_multiply.display()

print("\nScalar Division:")
result_scalar_division.display()

print("\nMatrix Power:")
result_power.display()
