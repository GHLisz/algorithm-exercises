class Solution:
    """
    @param: n: An integer
    @return: An integer
    """

    def numTrees(self, n):
        # write your code here
        dp = [0] * (n + 2)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
