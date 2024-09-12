#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates a n by n 2D matrix 90 degrees clockwise in place.
    """
    # Check if the matrix is a list of lists
    if not isinstance(matrix, list) or len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        return

    n = len(matrix)

    # Check if the matrix is square
    if not all(len(row) == n for row in matrix):
        return

    # Rotate the matrix in place
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Store the top element
            temp = matrix[i][j]
            # Move left element to top
            matrix[i][j] = matrix[n - 1 - j][i]
            # Move bottom element to left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Move right element to bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Assign top element to right
            matrix[j][n - 1 - i] = temp
