"""
46. Permutations
Medium


Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(res, nums, j):
            if j == len(nums):
                res.append(nums[:])
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(res, nums, j + 1)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        backtrack(res, nums, 0)
        return res
