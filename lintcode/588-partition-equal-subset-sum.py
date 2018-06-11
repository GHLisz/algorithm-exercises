class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """

    def canPartition(self, nums):
        # write your code here
        half, rem = divmod(sum(nums), 2)

        if rem: return False

        dp = [True] + [False] * half
        for num in nums:
            for i in range(half, 0, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]

        return dp[half]
