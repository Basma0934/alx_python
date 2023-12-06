def square_matrix_simple(matrix=[]):
    """Computing the square value of all integers of a matrix."""
    return ([list(map(lambda x: x * x, element)) for element in matrix])
