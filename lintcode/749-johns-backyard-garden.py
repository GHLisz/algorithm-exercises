class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        # Write your code here
        dp = [0] * 1001
        dp[:8] = [1, 0, 0, 1, 0, 0, 1, 1]

        for i in range(8, x + 1):
            if dp[i - 3] == 1 or dp[i - 7] == 1:
                dp[i] = 1

        if dp[x] == 1:
            return "YES"
        return "NO"
