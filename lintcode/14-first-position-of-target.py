class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        # write your code here
        low, high = 0, len(nums) - 1

        while low + 1 < high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1

        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        else:
            return -1
