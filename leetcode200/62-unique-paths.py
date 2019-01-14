"""
62. Unique Paths
Medium


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def sol1():  # dp
            dp = [1] * n
            for j in range(1, m):
                for i in range(1, n):
                    dp[i] += dp[i - 1]
            return dp[n - 1]

        def sol2():  # math, p = (m+n)! / (m! * n!)
            if 1 in (m, n):
                return 1

            from functools import reduce
            mul = lambda x, y: x * y
            return reduce(mul, range(n, n + m - 1)) // reduce(mul, range(1, m))

        return sol1()