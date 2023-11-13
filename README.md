# Matrix Operations and Unit Test

This Python project provides a `Matrix` class that supports basic matrix operations such as addition, subtraction, multiplication, scalar division, and matrix exponentiation. Additionally, it includes a unit test script to verify the correctness of the implemented operations.

## Matrix Class

The `Matrix` class is designed to handle various matrix operations. It includes the following functionalities:

- Addition (`__add__`)
- Subtraction (`__sub__`)
- Multiplication (`__mul__`)
- Scalar Division (`__truediv__`)
- Matrix Exponentiation (`__pow__`)
- Transposition (`transpose()`)
- Determinant Calculation (`determinant()`)
- Submatrix Extraction (`submatrix()`)

### Example Usage

```python
# Create matrices
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[2, 0], [1, 3]])

# Perform operations
result_add = matrix1 + matrix2
result_subtract = matrix1 - matrix2
result_multiply = matrix1 * matrix2
result_scalar_division = matrix1 / 2
result_power = matrix1 ** 2

# Display results
result_add.display()
result_subtract.display()
result_multiply.display()
result_scalar_division.display()
result_power.display()
```

## Unit Test

The `test_matrix_operations.py` script uses the `unittest` module to test the functionalities of the `Matrix` class. It covers basic operations and includes some invalid cases to ensure error handling.

### Running the Unit Test

To run the unit test, use the following command in the terminal:

```bash
python test_matrix_operations.py
```

If all tests pass, you should see an output indicating success. If there are issues, the output will provide information about the failed tests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```

In this `README.md`, I've included a brief description of the project, information about the `Matrix` class, example usage, details about the unit test script, and a section on how to run the unit test. Additionally, I mentioned that the project is licensed under the MIT License. You may want to include a `LICENSE.md` file with the actual license text.
