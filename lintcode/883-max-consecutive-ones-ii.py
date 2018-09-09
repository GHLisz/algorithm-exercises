class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        if not nums: return 0

        res, left, k, q = 0, 0, 1, []
        for right, val in enumerate(nums):
            if val == 0: q.append(right)
            if len(q) > k: left = q.pop(0) + 1
            res = max(res, right - left + 1)
        return res
