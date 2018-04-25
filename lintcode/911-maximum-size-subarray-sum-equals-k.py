class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        dic, res, total = {}, 0, 0
        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                res = max(res, i+1)
            if total - k in dic:
                res = max(res, i-dic[total - k])
            if total not in dic:
                dic[total] = i
        return res
