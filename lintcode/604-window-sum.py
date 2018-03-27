class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        if not nums or len(nums) < k:
            return []

        res, cursum, = [], 0

        cursum = sum(nums[:k])
        res.append(cursum)

        for i in range(k, len(nums)):
            cursum = cursum + nums[i] - nums[i - k]
            res.append(cursum)

        return res
