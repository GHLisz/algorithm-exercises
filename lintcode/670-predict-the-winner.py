class Solution:
    """
    @param nums: nums an array of scores
    @return: check if player 1 will win
    """

    def PredictTheWinner(self, nums):
        # write your code here
        dp = [0] * len(nums)
        for s in range(len(nums), -1, -1):
            for e in range(s + 1, len(nums)):
                a = nums[s] - dp[e]
                b = nums[e] - dp[e - 1]
                dp[e] = max(a, b)
        return dp[len(nums) - 1] >= 0
