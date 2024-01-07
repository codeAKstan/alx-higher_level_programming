#!/usr/bin/python3
"""
Task 2
A function that divides all elements of a matrix
return a new matrix
"""


def matrix_divided(matrix, div):
    """ matrix divided
    matrix must be a list of lists of integers or floats
    otherwise raise a TypeError exception with
    the message matrix must be a matrix (list of lists) of integers/floats
    """

    if not all(isinstance(row, list)
               and all(isinstance(element, (int, float))
                       for element in row) for row in matrix):
        raise
    TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2) for element in row]
                     for row in matrix]

    return result_matrix
