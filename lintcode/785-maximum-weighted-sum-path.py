class Solution:
    """
    @param nums:
    @return: nothing
    """

    def maxWeight(self, nums):
        # write your code here
        dp, m, n = [[0] * 200 for _ in range(200)], len(nums), len(nums[0])
        dp[0][m - 1] = nums[0][m - 1]

        for i in range(n):
            j = m - 1
            while j >= 0:
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + nums[i][j])
                if j < m - 1:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + nums[i][j])
                j = j - 1
        return dp[n - 1][0]
