class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        # write your code here
        lm, ln = len(matrix), len(matrix[0])
        f = [[0] * (ln + 1) for _ in range(lm + 1)]

        for i in range(1, lm + 1):
            for j in range(1, ln + 1):
                f[i][j] = f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1] + matrix[i - 1][j - 1]
                for m in range(i):
                    for n in range(j):
                        if f[i][j] == f[i][n] - f[m][n] + f[m][j]:
                            return [[m, n], [i - 1, j - 1]]
        return [[0, 0], [0, 0]]
