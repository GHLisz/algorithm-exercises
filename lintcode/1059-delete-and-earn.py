class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """

    def deleteAndEarn(self, nums):
        # write your code here
        total = [0] * 10002
        for i in range(len(nums)):
            total[nums[i]] += nums[i]
        for i in range(2, len(total)):
            total[i] = max(total[i - 1], total[i - 2] + total[i])
        return total[10001]
