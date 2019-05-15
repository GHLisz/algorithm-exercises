"""
78. Subsets
Medium


Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sol1():  # backtrack, recursive
            def backtrack(res, tmp, nums, start):
                res.append(tmp[:])
                for i in range(start, len(nums)):
                    tmp.append(nums[i])
                    backtrack(res, tmp, nums, i + 1)
                    tmp.pop()

            res = []
            backtrack(res, [], sorted(nums), 0)
            return res

        def sol2():  # combination, iterative
            res = [[]]
            for n in nums:
                for tmp in res[:]:
                    x = tmp[:]
                    x.append(n)
                    res.append(x)
            return res

        return sol1()
