class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums: return 0

        import math
        n = len(nums)
        left, right = [0] * n, [0] * n

        local_, global_ = 0, -math.inf
        for i, num in enumerate(nums):
            local_ = max(local_ + num, num)
            global_ = max(global_, local_)
            left[i] = global_

        local_, global_ = 0, -math.inf
        for i in range(n - 1, -1, -1):
            local_ = max(local_ + nums[i], nums[i])
            global_ = max(global_, local_)
            right[i] = global_

        res = -math.inf
        for i in range(n - 1):
            res = max(res, left[i] + right[i + 1])
        return res
