class Solution:
    """
    @param nums: the num arrays
    @return: the num arrays after rearranging
    """
    def rearrange(self, nums):
        # Write your code here
        nums.sort()
        res, n = [], len(nums)
        for i in range(n):
            if i % 2 == 0:
                res.append(nums[i//2])
            else:
                res.append(nums[i//2 + (n+1)//2])
        return res
