class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        n = len(nums)
        for i in range(1, n):
            if i % 2 == 1 and nums[i] < nums[i - 1] or \
                    i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
