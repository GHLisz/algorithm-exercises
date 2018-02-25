class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        n = len(nums)
        return int(0.5*n*(n+1)) - sum(nums)
