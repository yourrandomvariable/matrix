import unittest

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        # Create matrices for testing
        self.matrix1 = Matrix([[1, 2], [3, 4]])
        self.matrix2 = Matrix([[2, 0], [1, 3]])

    def test_addition(self):
        result = self.matrix1 + self.matrix2
        expected = Matrix([[3, 2], [4, 7]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_subtraction(self):
        result = self.matrix1 - self.matrix2
        expected = Matrix([[-1, 2], [2, 1]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_multiplication(self):
        result = self.matrix1 * self.matrix2
        expected = Matrix([[4, 6], [10, 12]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_scalar_division(self):
        result = self.matrix1 / 2
        expected = Matrix([[0.5, 1], [1.5, 2]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_matrix_power(self):
        result = self.matrix1 ** 2
        expected = Matrix([[7, 10], [15, 22]])
        self.assertEqual(result.matrix, expected.matrix)

    def test_invalid_addition(self):
        with self.assertRaises(ValueError):
            invalid_result = self.matrix1 + Matrix([[1, 2, 3], [4, 5, 6]])

    def test_invalid_multiplication(self):
        with self.assertRaises(ValueError):
            invalid_result = self.matrix1 * Matrix([[1, 2, 3], [4, 5, 6]])

if __name__ == '__main__':
    unittest.main()
