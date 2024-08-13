#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in place."""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap element at (i, j) with the element at (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        # Reverse each row to achieve the 90-degree rotation
        matrix[i].reverse()
