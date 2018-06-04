class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # write your code here
        res = cur_max = cur_min = nums[0]
        # cur_max, cur_min: max/min prd of subarray that ends with cur number A[i]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i])
            cur_min = min(nums[i], cur_min * nums[i])
            res = max(res, cur_max)

        return res
