class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end = end - 1
        return nums[start]
