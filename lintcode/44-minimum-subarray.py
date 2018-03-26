class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        min_ending_here = min_so_far = nums[0]
        for v in nums[1:]:
            min_ending_here = min(v, min_ending_here+v)
            min_so_far = min(min_so_far, min_ending_here)
        return min_so_far
