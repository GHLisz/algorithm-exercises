class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """

    def findTargetSumWays(self, nums, s):
        # Write your code here
        if not nums: return 0

        dp = [0] * 2001
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            nxt = [0] * 2001
            for total in range(-1000, 1001):
                if dp[total + 1000] > 0:
                    nxt[total + nums[i] + 1000] += dp[total + 1000]
                    nxt[total - nums[i] + 1000] += dp[total + 1000]
            dp = nxt
        return 0 if s > 1000 else dp[s + 1000]
