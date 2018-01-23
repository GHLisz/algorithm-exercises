class Solution:
    """
    @param: matrix: A lsit of lists of integers
    @return:
    """

    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        first_row = not all(matrix[0])
        first_col = not all(matrix[i][0] for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        if first_col:
            for i in range(m):
                matrix[i][0] = 0
