class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        n = len(nums)
        for i in range(n//2):
            nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
        return nums
