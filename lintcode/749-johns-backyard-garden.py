class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """

    def isBuild(self, x):
        # write you code here
        dp = [1, 0, 0, 1, 0, 0, 1, 1] + [0] * (1001 - 8)
        for i in range(8, x + 1):
            dp[i] = 1 if any(map(lambda x: dp[i - x] == 1, (3, 7))) else 0
        return 'YES' if dp[x] == 1 else 'NO'
