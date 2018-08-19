class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """

    def maxAreaOfIsland(self, grid):
        # Write your code here
        def dfs(grid, i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = -1
                return dfs(grid, i + 1, j) \
                       + dfs(grid, i, j + 1) \
                       + dfs(grid, i - 1, j) \
                       + dfs(grid, i, j - 1) \
                       + 1
            return 0

        m, n = len(grid), len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j))
        return res
