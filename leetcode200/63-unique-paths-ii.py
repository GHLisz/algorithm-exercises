"""
63. Unique Paths II
Medium


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        def sol1(grid):  # O(m*n) space
            if not grid:
                return
            r, c = len(grid), len(grid[0])
            dp = [[0] * c for _ in range(r)]
            dp[0][0] = 1 - grid[0][0]
            for i in range(1, r):
                dp[i][0] = dp[i - 1][0] * (1 - grid[i][0])
            for i in range(1, c):
                dp[0][i] = dp[0][i - 1] * (1 - grid[0][i])
            for i in range(1, r):
                for j in range(1, c):
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - grid[i][j])
            return dp[-1][-1]

        def sol2(grid):  # O(n) space
            if not grid:
                return
            r, c = len(grid), len(grid[0])
            cur = [0] * c
            cur[0] = 1 - grid[0][0]
            for i in range(1, c):
                cur[i] = cur[i - 1] * (1 - grid[0][i])
            for i in range(1, r):
                cur[0] *= (1 - grid[i][0])
                for j in range(1, c):
                    cur[j] = (cur[j - 1] + cur[j]) * (1 - grid[i][j])
            return cur[-1]

        def sol3(grid):  # in place
            if not grid:
                return
            r, c = len(grid), len(grid[0])
            grid[0][0] = 1 - grid[0][0]
            for i in range(1, r):
                grid[i][0] = grid[i - 1][0] * (1 - grid[i][0])
            for i in range(1, c):
                grid[0][i] = grid[0][i - 1] * (1 - grid[0][i])
            for i in range(1, r):
                for j in range(1, c):
                    grid[i][j] = (grid[i - 1][j] + grid[i][j - 1]) * (1 - grid[i][j])
            return grid[-1][-1]

        return sol3(obstacleGrid)
