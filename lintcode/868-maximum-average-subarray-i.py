class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """

    def findMaxAverage(self, nums, k):
        # Write your code here
        res = total = sum(nums[:k])
        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            res = max(total, res)
        return res / k
