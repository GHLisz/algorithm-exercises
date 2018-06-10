class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber2(self, nums):
        # write your code here
        if len(nums) < 3: return max(nums, default=0)
        last1, now1, last2, now2 = 0, 0, 0, 0
        for n in nums[1:]:
            last1, now1 = now1, max(last1 + n, now1)
        for n in nums[:-1]:
            last2, now2 = now2, max(last2 + n, now2)
        return max(now1, now2)
