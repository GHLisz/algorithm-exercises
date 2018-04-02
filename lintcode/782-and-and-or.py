class Solution:
    """
    @param n:
    @param nums: 
    @return: return the sum of maximum OR sum, minimum OR sum, maximum AND sum, minimum AND sum.
    """
    def getSum(self, n, nums):
        # write your code here
        max_or_sum = max_and_sum = min_or_sum = min_and_sum = nums[0]
        for i in range(1, n):
            max_or_sum |= nums[i]
            max_and_sum = max(max_and_sum, nums[i])
            min_or_sum = min(min_or_sum, nums[i])
            min_and_sum &= nums[i]
        return sum([max_or_sum, max_and_sum, min_or_sum, min_and_sum])
