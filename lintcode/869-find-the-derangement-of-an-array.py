class Solution:
    """
    @param n: an array consisting of n integers from 1 to n
    @return: the number of derangement it can generate
    """

    def findDerangement(self, n):
        # Write your code here
        if n < 2: return 0

        dp = [0] * (n + 1)
        dp[1], dp[2] = 0, 1

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) * (i - 1) % (10 ** 9 + 7)

        return dp[n]
