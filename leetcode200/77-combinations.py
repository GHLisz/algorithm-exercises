"""
77. Combinations
Medium


Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def sol1():  # backtrack
            def backtrack(n, k, pos, tmp, res):
                if k == len(tmp):
                    res.append(tmp[:])
                    return
                for i in range(pos, n + 1):
                    tmp.append(i)
                    backtrack(n, k, i + 1, tmp, res)
                    tmp.pop()

            res = []
            backtrack(n, k, 1, [], res)
            return res

        def sol2():  # iterative
            combs = [[]]
            for _ in range(k):
                combs = [[i] + c for c in combs
                         for i in range(1, c[0] if c else n + 1)]
            return combs

        return sol2()
