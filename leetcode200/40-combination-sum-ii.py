"""
40. Combination Sum II
Medium


Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(nums, res, temp, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                res.append(temp[:])
            else:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    temp.append(nums[i])
                    backtrack(nums, res, temp, remain - nums[i], i + 1)
                    temp.pop()

        candidates.sort()
        res = []
        backtrack(candidates, res, [], target, 0)
        return res
