class Solution:
    """
    @param nums: an array
    @return: the corresponding expression in string format
    """

    def optimalDivision(self, nums):
        # Write your code here
        nums = list(map(str, nums))
        if len(nums) <= 2: return '/'.join(nums)
        return f"{nums[0]}/({'/'.join(nums[1:])})"
