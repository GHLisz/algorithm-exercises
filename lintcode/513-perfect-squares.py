class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        dp = [float('inf')] * (n + 1)

        i = 1
        while i ** 2 <= n:
            dp[i ** 2] = 1
            i += 1

        for i in range(1, n + 1):
            j = 1
            while i + j ** 2 <= n:
                dp[i + j ** 2] = min(dp[i] + 1, dp[i + j ** 2])
                j += 1

        return dp[n]
