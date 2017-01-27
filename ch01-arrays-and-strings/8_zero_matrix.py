"""1.8 Zero Matrix:  Write an algorithm such that if an element is an MxN
matrix is 0, its entire row and column are set to 0."""

def zero_matrix(matrix):
    """Function that if it finds an element with a zero, it replaces that
    elements row and column with zerios.
        >>> zero_matrix([])
        []
        >>> zero_matrix([[0]])
        [[0]]
        >>> zero_matrix([[1], [0]])
        [[0], [0]]
        >>> zero_matrix([[1, 0]])
        [[0, 0]]
        >>> zero_matrix([[1, 2, 3], [1, 0, 4]])
        [[1, 0, 3], [0, 0, 0]]
        >>> zero_matrix([[1, 0], [1, 1], [0, 1]])
        [[0, 0], [0, 0], [0, 0]]
    """
    # Check if matrix is empty:
    if not matrix:
        return matrix

    # Create variables to represent dimensions of MxN matrix
    m = len(matrix)
    n = len(matrix[0])

    # Create sets to hold row and column indices that contain zeroes
    rows_with_zeroes = set()
    cols_with_zeroes = set()

    # Populate the row and column sets
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_with_zeroes.add(i)
                cols_with_zeroes.add(j)

    for i in range(m):
        if i in rows_with_zeroes:
            for j in range(n):
                matrix[i][j] = 0

    for j in range(n):
        if j in cols_with_zeroes:
            for i in range(m):
                matrix[i][j] = 0

    return matrix


########################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    print
    if not result.failed:
        print "Great job, you completed zero matrix!"
    print
