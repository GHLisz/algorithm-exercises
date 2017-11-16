class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        l = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        return nums
