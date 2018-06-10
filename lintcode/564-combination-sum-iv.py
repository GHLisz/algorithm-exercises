class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        # write your code here
        nums.sort()
        # dp[i]: number of possibles when target is i
        dp = [1] + [0] * target

        for i in range(1, target + 1):
            for n in nums:
                if i < n: break
                dp[i] += dp[i - n]

        return dp[-1]
