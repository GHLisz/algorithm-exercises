"""
15. 3Sum
Medium


Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, nums = [], sorted(nums)

        for k in range(len(nums) - 2):
            if nums[k] > 0:
                continue
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            target = 0 - nums[k]
            i, j = k + 1, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i, j = i + 1, j - 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return res
