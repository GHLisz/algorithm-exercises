"""
90. Subsets II
Medium


Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def sol1():
            def backtrack(res, tmp, nums, start):
                res.append(tmp[:])
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    tmp.append(nums[i])
                    backtrack(res, tmp, nums, i + 1)
                    tmp.pop()

            res = []
            backtrack(res, [], sorted(nums), 0)
            return res

        def sol2():
            res = [[]]
            nums.sort()

            size, start = 0, 0
            for i, n in enumerate(nums):
                start = size if i > 0 and nums[i] == nums[i - 1] else 0
                size = len(res)
                for j in range(start, size):
                    x = res[j][:]
                    x.append(n)
                    res.append(x)
            return res

        return sol1()
