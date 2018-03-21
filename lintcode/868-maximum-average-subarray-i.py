class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        # Write your code here
        res = sum_ = sum(nums[:k])
        for i in range(k, len(nums)):
            sum_ += nums[i] - nums[i-k]
            res = max(sum_, res)
        return res/float(k)
