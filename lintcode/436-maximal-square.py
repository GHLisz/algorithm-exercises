class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

    def maxSquare(self, matrix):
        # write your code here
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        maxsqlen = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = 1 + min(
                        min(dp[i][j - 1], dp[i - 1][j]),
                        dp[i - 1][j - 1])
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen ** 2
