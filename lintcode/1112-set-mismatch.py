class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        dup, mis = -1, 1
        for n in nums:
            if nums[abs(n)-1] < 0:
                dup = abs(n)
            else:
                nums[abs(n)-1] *= -1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                mis = i+1
        return [dup, mis]
