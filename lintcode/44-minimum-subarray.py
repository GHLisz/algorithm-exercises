class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        sum_, min_ = 0, 999999
        for num in nums:
            sum_ = 0 if sum_ > 0 else sum_
            sum_ += num
            min_ = min(sum_, min_)
        return min_
