"""
1. Two Sum
Easy


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx_map = {}
        for idx, num in enumerate(nums):
            if target - num in num_idx_map.keys():
                return [num_idx_map[target - num], idx]
            num_idx_map[num] = idx
        return [-1, -1]
