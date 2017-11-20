class Solution:
    """
    @param: n: non-negative integer, n posts
    @param: k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        dp = [0, k, k*k, 0]
        if n <= 2:
            return dp[n]
        for i in range(2, n):
            dp[3] = (k-1) * (dp[1] + dp[2])
            dp[1], dp[2] = dp[2], dp[3]
        return dp[3]
