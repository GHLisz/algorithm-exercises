class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """

    def findDuplicates(self, nums):
        # write your code here
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(abs(idx + 1))
            nums[idx] *= -1
        return sorted(res)
