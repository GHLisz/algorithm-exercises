class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == n == 1: return 1
        dp = [[0]*m for _ in range(n)]
        for col in range(m):
            dp[0][col] = 1
        for row in range(n):
            dp[row][0] = 1
        for col in range(1, m):
            for row in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]
