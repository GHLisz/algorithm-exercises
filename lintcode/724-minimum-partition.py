class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """

    def findMin(self, nums):
        # write your code here
        total = sum(nums)
        dp = [True] + [False] * (total // 2)
        for n in nums:
            for j in range(total // 2, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]
        return total - 2 * next((i for i in range(len(dp) - 1, -1, -1) if dp[i]), 0)
