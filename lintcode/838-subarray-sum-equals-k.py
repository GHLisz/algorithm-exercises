class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        dic, res, total = {0: 1}, 0, 0
        for i in range(len(nums)):
            total += nums[i]
            res += dic.get(total - k, 0)
            dic[total] = dic.get(total, 0) + 1
        return res
