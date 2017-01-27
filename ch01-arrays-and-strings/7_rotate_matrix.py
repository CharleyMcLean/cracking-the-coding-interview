"""1.7 Rotate Matrix:  Given an image represented by an NxN matrix, where
each pixel in the image is 4 bytes, write a method to rotate the image by
90 degrees.  Can you do this in place?
"""


def rotate_image(pixel_matrix):
    """Function which takes in an NxN array representing an image of pixels.
    Image matrix is rotated clockwise by 90 degrees and saved as a new matrix.
        >>> rotate_image([])
        []
        >>> rotate_image(['a'])
        ['a']
        >>> rotate_image([['a', 'b'], ['c', 'd']])
        [['c', 'a'], ['d', 'b']]
        >>> rotate_image([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
        [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f', 'c']]
    """
    # Capture length of matrix for later use.
    n = len(pixel_matrix)

    # if length is 0 or 1, the original matrix will be returned.
    if n == 0 or n == 1:
        return pixel_matrix

    # Construct new matrix to hold rotated image.
    new_matrix = []
    for i in range(n):
        new_matrix.append([0] * n)

    # Pixels are moved from [i][j] in orig matrix to [j][n-1-i] in new matrix
    for i in range(n):
        for j in range(n):
            new_matrix[j][n - 1 - i] = pixel_matrix[i][j]

    return new_matrix


def rotate_image_in_place(pixel_matrix):
    """Function which takes in an NxN array representing an image of pixels.
    Image matrix is rotated clockwise by 90 degrees and changed in place.
        >>> rotate_image([])
        []
        >>> rotate_image(['a'])
        ['a']
        >>> rotate_image([['a', 'b'], ['c', 'd']])
        [['c', 'a'], ['d', 'b']]
        >>> rotate_image([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
        [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f', 'c']]
    """
    pass

#########################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    print
    if not result.failed:
        print "Great job, all tests passed!"
    print