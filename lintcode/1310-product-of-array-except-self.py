class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """

    def productExceptSelf(self, nums):
        # write your code here
        res, n = [], len(nums)
        left, right = 1, 1

        for i in range(n):
            res.append(left)
            left *= nums[i]
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
