class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and nums[mid - 1] != target:
                return mid
            elif nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
