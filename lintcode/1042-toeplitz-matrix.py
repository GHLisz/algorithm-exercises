class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """

    def isToeplitzMatrix(self, matrix):
        # Write your code here
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
