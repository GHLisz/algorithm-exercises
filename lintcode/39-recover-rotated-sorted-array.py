class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        for index in range(0, len(nums)-1):
            if nums[index] > nums[index+1]:
                self.reverse(nums, 0, index)
                self.reverse(nums, index+1, len(nums)-1)
                self.reverse(nums, 0, len(nums)-1)
