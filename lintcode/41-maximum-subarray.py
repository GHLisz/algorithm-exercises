class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        global_ = local = nums[0]

        for i in range(1, len(nums)):
            local = max(nums[i], local + nums[i])
            global_ = max(local, global_)

        return global_
