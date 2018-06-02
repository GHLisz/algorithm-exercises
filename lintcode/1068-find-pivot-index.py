class Solution:
    """
    @param nums: an array
    @return: the "pivot" index of this array
    """
    def pivotIndex(self, nums):
        # Write your code here
        left, right = 0, sum(nums)
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
        return -1
