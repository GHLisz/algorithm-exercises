class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        import math
        dp = [math.inf] * (n + 1)

        i = 1
        while i * i <= n:
            dp[i * i] = 1
            i += 1

        for i in range(1, n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1

        return dp[n]
