class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the number of subarrays where the product of all the elements in the subarray is less than k
    """

    def numSubarrayProductLessThanK(self, nums, k):
        # Write your code here
        if k <= 1: return 0
        ans, left, prd = 0, 0, 1
        for right, val in enumerate(nums):
            prd *= val
            while prd >= k:
                prd //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
