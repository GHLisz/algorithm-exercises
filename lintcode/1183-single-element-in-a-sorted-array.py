class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """

    def singleNonDuplicate(self, nums):
        # write your code here
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
