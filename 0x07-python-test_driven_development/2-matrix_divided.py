#!/usr/bin/python3
"""Fx to divide all objects of a matrix"""


def matrix_divided(matrix, div):
    """Method to divide the objents
    Arguments: matrix, div.
    Raises: Errors depends on the case.
    Returns: objents divided
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    if len(matrix[0]) is 0:
        raise TypeError(err1)

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError(err2)
        for obj in row:
            if type(obj) not in (int, float):
                raise TypeError(err1)

    if type(div) not in (int, float):
        raise TypeError(err3)

    if div is 0:
        raise ZeroDivisionError(err4)

    return [[round((obj / div), 2) for obj in row] for row in matrix]
