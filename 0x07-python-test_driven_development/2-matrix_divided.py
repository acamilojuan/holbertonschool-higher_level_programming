#!/usr/bin/python3
"Function to print divided numbers"


def matrix_divided(matrix, div):
    """Arguments
    matrix: list of integers to be used
    div: Number that divides
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    leng = len(matrix[0])
    if leng is 0:
        raise TypeError(error_type_matrix)

    for row in matrix:
        if leng != len(row):
            raise TypeError(error_length)
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_type_matrix)
        
    if type(div) is not int and type(div) is not float:
        raise TypeError(error_type_div)
    if div is 0:
        raise ZeroDivisionError(error_div_zero)
    new_matrix = [[round(float(element)/float(div), 2) for element in row]
                for row in matrix]
    
    return new_matrix
