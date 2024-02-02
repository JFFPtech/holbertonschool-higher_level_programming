#!/usr/bin/python3
"""
Matrix division module.

This module contains a function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        A new matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If the rows of the matrix are not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.

    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(type(num) in [int, float] for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
