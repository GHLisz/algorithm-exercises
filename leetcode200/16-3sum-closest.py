"""
16. 3Sum Closest
Medium


Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res, nums = None, sorted(nums)

        for k in range(len(nums) - 2):
            l, r = k + 1, len(nums) - 1

            while l < r:
                total = nums[k] + nums[l] + nums[r]

                if res is None or abs(total - target) < abs(res - target):
                    res = total

                if total == target:
                    return total
                elif total < target:
                    l += 1
                else:
                    r -= 1
        return res
