class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                reverse(nums, 0, i)
                reverse(nums, i + 1, len(nums) - 1)
                reverse(nums, 0, len(nums) - 1)
