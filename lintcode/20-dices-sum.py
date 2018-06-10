class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        dp = [[0] * (6 * n + 1) for _ in range(n + 1)]
        # dp[i][j]: probability when dice count is i, and sum is j
        for i in range(1, 7):
            dp[1][i] = 1.0 / 6.0

        for i in range(2, n + 1):
            for j in range(i, 6 * n + 1):
                for k in range(1, 7):
                    if j > k:
                        dp[i][j] += dp[i - 1][j - k]
                dp[i][j] /= 6.0

        return [(i, dp[n][i]) for i in range(n, 6 * n + 1)]
