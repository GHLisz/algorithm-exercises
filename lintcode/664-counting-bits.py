class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """

    def countBits(self, num):
        # write your code here
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
