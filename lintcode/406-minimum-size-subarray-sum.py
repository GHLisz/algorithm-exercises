class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        res, n = float('inf'), len(nums)
        left, total = 0, 0
        for i in range(n):
            total += nums[i]
            while total >= s:
                res = min(res, i-left+1)
                total -= nums[left]
                left += 1
        return res if res != float('inf') else -1
