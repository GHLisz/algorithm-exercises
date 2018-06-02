class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
