class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        max_sum, min_sum, real_sum = nums[0], 0, 0

        for num in nums:
            real_sum += num
            max_sum = real_sum - min_sum if real_sum - min_sum > max_sum else max_sum
            min_sum = real_sum if real_sum < min_sum else min_sum

        return max_sum
